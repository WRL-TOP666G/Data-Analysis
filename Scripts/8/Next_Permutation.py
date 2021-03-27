def next_permutation(t):
    '''
        Next Permutation
        Given a permutation of any length,
         generate the next permutation in lexicographic order. 
         For example, this are the permutations for [1,2,3] in lexicographic order.

        >>> list(it.permutations([1,2,3]))
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] 
        Then, your function next_permutation(t:tuple)->tuple should do the following

        >>> next_permutation((2,3,1))
        (3,1,2) 
        Because (3,1,2) is the next permutation in lexicographic order. Here is another example:

        >>> next_permutation((0, 5, 2, 1, 4, 7, 3, 6))
        (0, 5, 2, 1, 4, 7, 6, 3) 
        Your function should work for very long input tuples so
         the autograder will time-out if you try to brute force your solution. 
         The last permutation should wrap aruond to the first.

        >>> next_permutation((3,2,1,0))
        (0, 1, 2, 3) 

    ''' 
    assert isinstance(t, tuple) and len(t)>0
    assert len(set(t))==len(t)
    for i in t:
        assert isinstance(i, int) and i>=0
    nums=list(t)
    i = len(nums)-1
    while i>0:
        if nums[i-1]<nums[i]:
            break
        i = i-1
    i = i-1
    j = len(nums)-1
    while j>i:
        if nums[j]>nums[i]:
            break
        j=j-1
    nums[i],nums[j]=nums[j],nums[i]  
    nums[i+1:]=sorted(nums[i+1:]) 
    return tuple(nums)
        
        
