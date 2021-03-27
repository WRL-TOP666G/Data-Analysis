def multinomial_sample(n,p,k=1):  
    '''
    Write a function to return samples from the Multinomial distribution using pure Python 
    (i.e., no third-party modules like Numpy, Scipy). Here is some sample output.

    >>> multinomial_sample(10,[1/3,1/3,1/3],k=10)
    [[3, 3, 4], 
    [4, 4, 2], 
    [3, 4, 3], 
    [5, 2, 3], 
    [3, 3, 4], 
    [3, 4, 3], 
    [6, 2, 2], 
    [2, 6, 2], 
    [5, 4, 1], 
    [4, 4, 2]] 
    

    Here is your function signature
    def multinomial_sample(n,p,k=1):  
                                                                          
            Return samples from a multinomial distribution.                     
                                                                                
            n:= number of trials                                                
            p:= list of probabilities                                           
            k:= number of desired samples                                       
                                                                            
    
    '''
    import random
    assert isinstance(n,int) and n>0
    assert isinstance(p,list) and abs(1-sum(p))<1e-7
    for i in p:
        assert isinstance(i, float) or isinstance(i, int)
    
    assert isinstance(k,int) and k>0
    l=[]
    for i in range(k):
        tmp=[]
        num=len(p)
        a=0
        add=0
        tmpN=n
        for j in range(num-1):
            a=random.randrange(0, tmpN)
            add+=a
            tmpN-=a
            tmp.append(a)
        c=n-add
        tmp.append(c)
        l.append(tmp)
    return l