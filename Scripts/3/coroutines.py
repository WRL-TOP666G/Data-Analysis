def tracker(p,limit=2):
    '''
    Coroutines are generalization of subroutines. They are used for cooperative multitasking where a process voluntarily yield (give away) control periodically or when idle in order to enable multiple applications to be run simultaneously
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
    
        

    
