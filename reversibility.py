import itertools

def xor_combine(sez):
    while len(sez) > 1:
        a = sez.pop()
        b = sez.pop()
        
        sez.append(a ^ b)
    
    return sez.pop()
    

#input is list of 0 and 1 where input[0] = x^max
#exponents are indexes of which indexes we should use
def lfsr(input, exponents):
        
        #values of the input that we will xor
        values = [input[i] for i in exponents]
        
        #shift the input bits by 1 to the right and insert a combined xor at the beginning
        return (xor_combine(values), input[0], input[1], input[2], input[3], input[4], input[5], input[6])


#generates all possible polynomials or rather creates all the possible combinations of chosen exponents
def all_polynomials():
    
    #iterate from 1 to 255
    for i in range(1,256):
    
        #convert to binary and chop away the starting 0b notation
        binary = [int(x) for x  in bin(i).split("0b")[1]]
        
        #bin converts number to binary without leading 0s
        #we work with 8 bits so we want to add leading 0s to any number that doesn't have them
        while len(binary) < 8:
            binary.insert(0, 0)
        
        #now we have to extract on which index the 1s appear
        indexes = [i for i in range(len(binary)) if binary[i] == 1]
        
        #we have the indexes of the exponents, yield them now
        yield indexes

if __name__ == "__main__":
    x = [True, False]
    all_inputs = list(itertools.product(x, repeat=8))
    
    reversible_polynomials = []
    
    #iterate over all the polynomials
    for exponents in all_polynomials():
        
        all_outputs = set()
        
        #iterate over all the inputs
        for input in all_inputs:
            
            #calculate one lfsr shift for the given input and the given polynomial
            output = lfsr(input, exponents)
            
            #add the output to the set
            all_outputs.add(output)
        
        
        #now check if the lfsr with a given polynomial is reversable => has the same number of unique outputs as inputs
        if len(list(all_outputs)) == len(all_inputs):
            reversible_polynomials.append(exponents)
            print("The polynomial with the exponents:", exponents, "is reversible")
            print("-------------------------------------------------------------------------------")
    
    
    print("*******************************************************************************")
    print("Out of a total of 255 polynomials,", len(reversible_polynomials), "are reversible")