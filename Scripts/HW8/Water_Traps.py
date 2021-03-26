def get_trapped_water(seq):
    '''
        Water Traps
        You are given an array of non-negative integers that
         represents a two-dimensional elevation map where each element is unit-width wall and
          the integer value is the height. Suppose rain fills all available gaps between two bordering walls.

        Compute how many units of water remain trapped between the walls in the map.

        For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
         Here's another example for the sequence [3, 0, 1, 3, 0, 5] where the answer is 8,
        Example

        Here is the function signature get_trapped_water(seq) where seq is an input list,
         as in the examples.
    '''
    assert isinstance(seq,list) and len(seq)>0
    for num in seq:
        assert isinstance(num, int) and num>=0
    r=len(seq)-1
    l=0
    ans=0
    l_max=0
    r_max=0
    while l<r:
        if seq[l]<seq[r]:
            if l_max>seq[l]:
                ans+=(l_max-seq[l])
            else:
                l_max=seq[l]
            l+=1
        else:
            if r_max>seq[r]:
                ans+=(r_max-seq[r])
            else:
                r_max=seq[r]
            r-=1
    return ans