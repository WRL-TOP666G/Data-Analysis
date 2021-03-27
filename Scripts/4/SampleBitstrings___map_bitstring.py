def map_bitstring(x):
    '''
        Write a function map_bitstring that takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1. The output of your function is a dictionary of the so-described key-value pairs.

        Here is an example:
        >>> x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
        >>> map_bitstring(x) 
        { '100': 0, '110': 1, '010': 0, '111': 1, '000': 0, '011': 1} 
    '''
    assert isinstance(x, list)
    for key in x:
        assert isinstance(key, str)
        for i in key:
            assert i=='0' or i=='1'
    s=set(x)
    ans={}
    for key in s:
        one=0
        zero=0
        for i in key:
            if i=='0':
                zero+=1
            else: 
                one+=1
        if zero>one:
            ans[key]=0
        else: 
            ans[key]=1
    return ans

