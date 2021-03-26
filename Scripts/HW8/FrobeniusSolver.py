def solvefrob(coefs,b):
    '''
        Frobenius Solver
        The Frobenius equation is the Diophantine equation,

        a_1 x_1 +... + a_n x_n = b

        where a_i> 0 are positive integers, b> 0 is a positive integer, 
        and the solution x_i consists of non-negative integers. Here is a sample run,

        >>> solvefrob([1,2,3,5],10) 
        [(0, 0, 0, 2), 
        (0, 1, 1, 1), 
        (0, 2, 2, 0), 
        (0, 5, 0, 0), 
        (1, 0, 3, 0), 
        (1, 2, 0, 1), 
        (1, 3, 1, 0), 
        (2, 0, 1, 1), 
        (2, 1, 2, 0), 
        (2, 4, 0, 0), 
        (3, 1, 0, 1), 
        (3, 2, 1, 0), 
        (4, 0, 2, 0), 
        (4, 3, 0, 0), 
        (5, 0, 0, 1), 
        (5, 1, 1, 0), 
        (6, 2, 0, 0), 
        (7, 0, 1, 0), 
        (8, 1, 0, 0), 
        (10, 0, 0, 0)] 
        
        Hint: Use Numpy broadcasting effectively. 
        There is a timeout in the test-case, so if it takes too long to compute 
        (e.g, you used too many for loops), it will be marked wrong. 
        The function signature is solvefrob(coefs,b) where coefs is the list of a_i coefficients. 
        You can only use Numpy for this problem. No other third party packages.
    '''
    assert isinstance(coefs,list) and len(coefs)>0
    assert isinstance(b, int) and b>0
    for num in coefs:
        assert isinstance(num, int) and num>0
   