def count_paths(m,n,blocks):
    '''
        Grid Path Searching
            A two dimensional grid has M horizontal rows and N vertical columns. Let 
            (i,j)denote the square at the 
            (i + 1) t h row from the top and the 
            (j + 1 ) t h column from the left i.e., they are 0-indexed.

            Within the grid, for each 
            i and  j ( 0 ≤ i ≤ M − 1 ,  0 ≤ j ≤ N − 1), there can only be two symbols # and . 
            where # denotes a blockage and . denotes a passable opening. 
            Starting at the upper left and only moving downwards and rightwards, 
            find the number of connected paths between 
            the top-left square and the bottom right square by traversing only the intermediate squares with the . symbol. The start and end positions are never be marked with #.

            Example:

            M=3 and N=4
            ...#
            .#..
            ....
            calling count_paths(3,4,[(0,3),(1,1)]) returns the answer is 3.
            Here is the function signature: count_paths(m,n,blocks) 
            where m is the number of rows and n is the number of columns. 
            The blocks variable is a list of tuples indicating the blocked # entries in the grid.
    '''
    assert isinstance(m,int) and m>0
    assert isinstance(n,int) and n>0
    assert isinstance(blocks,list) and len(blocks)>0
    for t in blocks:
        assert isinstance(t, tuple) and len(t)==2
        assert isinstance(t[0], int) and t[0]>=0 and t[0]<m
        assert isinstance(t[1], int) and t[1]>=0 and t[1]<n

    arr=[[0 for j in range(n)] for i in range(m)]
    for pos in blocks:
        arr[pos[0]][pos[1]]=-1
    if arr[0][0]!=-1:
        arr[0][0]=1
    else:
        arr[0][0]=0
    for i in range(1,m):
        if arr[i][0]!=-1:
            arr[i][0]=arr[i-1][0]
        else: 
            arr[i][0]=0
            
    for j in range(1,n):
        if arr[0][j]!=-1:
            arr[0][j]=arr[0][j-1]
        elif arr[0][j]==-1: 
            arr[0][j]=0
    for i in range(1,m):
        for j in range(1,n):
            if arr[i][j]!=-1:
                arr[i][j]=arr[i-1][j]+arr[i][j-1]
            else:
                arr[i][j]=0
    return arr[m-1][n-1]
        
