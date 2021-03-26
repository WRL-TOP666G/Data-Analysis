def tracker(p,limit=2):
    '''
        The Fibonacci numbers are defined by the following recursion: F[n] = F[n-1]+F[n-2] with initial values F[1]=F[0]=1. Write a generator to compute the first n Fibonacci numbers. For example, for n=10, the output for list(fibonacci(n)) should be [1,1,2,3,5,8,13,21,34,55].
    '''
    from types import GeneratorType
    assert isinstance(p,GeneratorType)
    assert isinstance(limit,int) and limit>0
    cnt=0
    while True:
        val=next(p).seconds%2
        if val%2:
            cnt+=1
        rval= yield cnt
        if rval is not None:
            assert isinstance(rval,int) and rval>0
            limit=rval
        if cnt>=limit: break
    
        

    
