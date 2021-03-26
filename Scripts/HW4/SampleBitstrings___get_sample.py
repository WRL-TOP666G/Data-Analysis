def get_sample(nbits=3,prob=None,n=1):
    '''
        Problem: Random samples for a finite population of bitstrings
        Given a number of bits, write the get_sample function to return a list n of random samples from a finite probability mass function defined by a dictionary with keys defined by a specified number of bits. For example, given 3 bits, we have the following dictionary that defines the probability of each of the keys. The values of the dictionary correspond of the probability of drawing any one of these. For example, if all of these were equally likely, then here is the corresponding dictionary p,

         p={'000': 0.125,
         '001': 0.125,
         '010': 0.125,
         '011': 0.125,
         '100': 0.125,
         '101': 0.125,
         '110': 0.125,
         '111': 0.125}
         
        Your get_sample function should return something like the following,

         >>> get_sample(nbits=3,prob=p,n=4)
        ['101', '000', '001', '100']
        Hint: Validate your inputs thoroughly.

        Function signature: get_sample(nbits=3,prob=None,n=1). Keep the default values as given in the function signature.
    '''
    import random
    assert isinstance(nbits, int) and nbits>0
    assert isinstance(n, int) and n>0
    if prob!=None:
        assert isinstance(prob, dict)
        for key, value in prob.items():
            assert isinstance(key, str)
            for i in key:
                assert i=='0' or i=='1'
            assert isinstance(value, int) or isinstance(value, float)
            assert value>=0 and value<=1
        assert sum(prob.values())==1.0
    
    ans=[]
    number=2**nbits
    if prob is None:
        prob={}
        probability= 1.0/number
        for i in range(number):
            bit=str(bin(i)[2:])
            while len(bit)!=nbits:
                bit='0'+bit
            prob[bit]=probability

    for i in range(n):
        bit=str(bin(random.randint(0,number-1))[2:])
        while len(bit)!=nbits:
            bit='0'+bit
        while bit in ans:
            bit=str(bin(random.randint(0,number-1))[2:])
            while len(bit)!=nbits:
                bit='0'+bit
        ans.append(bit)
    return ans
        
