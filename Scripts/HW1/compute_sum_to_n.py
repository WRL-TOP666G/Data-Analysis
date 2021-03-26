def compute_sum_to_n(n):
    '''
    Write a function that computes the sum of all non-negative integers (i.e. >=0) up to 
    and including a specified value, n. Here is the function signature compute_sum_to_n(n).
    
    :param n: input non-neg 
    :type n: int
    :return: int
    '''
    assert isinstance(n, int)
    assert n>=0
    sum=0
    while n>=0:
        sum+=n
        n=n-1
    return sum

