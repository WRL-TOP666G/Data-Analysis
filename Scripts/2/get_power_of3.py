def get_power_of3(n):
    '''
        Given a set of weights {1,3,9,27}, write a function to construct any number between 1 and 40. 
        In other words, using the set above and the addition and subtraction operations, 
        construct any integer between 1 and 40 without re-using elements. 
        For example, 4 = 1+1+1+1 is not acceptable.
    
        For example, 8 = 9 - 1 10 = 1 + 9
        Hint: see the itertools module. Your function should return a 4-element list of the decomposition. 
        For example, your return value given input 10 should be [1,0,1,0] because 1*1 + 0*3 + 9*1 + 27*0=10. 
        Name your function get_power_of3.
    '''
    assert isinstance(n,int)
    assert n>0 and n<=40
    l1=[-1,0,1]
    l3=[-3,0,3]
    l9=[-9,0,9]
    l27=[-27,0,27]
    for i in range(len(l1)):
        for j in range(len(l3)):
            for k in range(len(l9)):
                for l in range(len(l27)):
                    if l1[i]+l3[j]+l9[k]+l27[l] == n:
                        return [i-1,j-1,k-1,l-1]

    
