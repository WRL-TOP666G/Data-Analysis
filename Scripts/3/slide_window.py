def slide_window(x,width,increment):
    '''
        Implement a sliding window for an arbitrary input list. The function should take the window width and the window increment as inputs and should produce a sequence of overlapping lists from the input list. For example, given x=range(15), the following is the output given a window width of 5 and window increment of 2.

        [[0, 1, 2, 3, 4],
         [2, 3, 4, 5, 6],
         [4, 5, 6, 7, 8],
         [6, 7, 8, 9, 10],
         [8, 9, 10, 11, 12],
         [10, 11, 12, 13, 14]]

        In the event that the input parameters do not yield a complete set of even sublists, just truncate the ragged tail. For example,

        >>> slide_window(range(18),5,2)
        [[0, 1, 2, 3, 4],
         [2, 3, 4, 5, 6],
         [4, 5, 6, 7, 8],
         [6, 7, 8, 9, 10],
         [8, 9, 10, 11, 12],
         [10, 11, 12, 13, 14],
         [12, 13, 14, 15, 16]]
    '''

    assert isinstance(x,list)
    assert isinstance(width,int)
    assert isinstance(increment,int)
    assert width>0
    assert increment>0
    n=len(x)
    print()
    l=[]
    add=0
    while add*increment+width<=n:
        tmp=[]
        for i in range(width):
            tmp.append(x[i+add*increment])
        if len(tmp)==width:
            l.append(tmp)
        add+=1
    
    return l
