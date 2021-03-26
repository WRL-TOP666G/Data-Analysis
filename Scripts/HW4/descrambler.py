def  descrambler(w,k):
    '''
        You are given a sequence of n lower-case letters and a k-tuple of integers that 
        indicate partition-lengths of the sequence. 
        Also, you have a dictionary of commonly used words. 
        The n letters represent a phrase of k words where the length of the jth word is the jth element of the tuple.

        Here is an example: w = 'trleeohelh' , k=(5,5).
        Your generator descrambler(w,k) should iteratively yield 
        the output ['hello three','three hello','hello there','there hello']. 
        Note that because both words have 5 characters, 
        it is not possible to definitively know the order of the phrase.

        Here are more interesting examples:

        >>> list(descrambler('choeounokeoitg',(3,5,6)))
        ['one tough cookie',
        'one ought cookie',
        'neo tough cookie',
        'neo ought cookie']
        >>> list(descrambler('qeodwnsciseuesincereins',(4,7,12)))
        ['wise insider consequences']
        
        Hints

        Use a hash-map to process the input file of valid words
        The order of the strings in the output sequence is irrelevent.
        Within each output string, the order of words should follow the sequence of word-lengths in k.
        Use itertools.
        The autograder may time out if your solution is too slow.
        The word list above is in a file /tmp/google-10000-english-no-swears.txt on the autograder.
    '''
    from collections import defaultdict
    from itertools import permutations
    #assert
    assert isinstance(w,str)
    assert isinstance(k,tuple)
    assert type(sum(k))== type(len(w)) and sum(k)==len(w)
    for i in k:
        assert i>0
    #Read word file
    folder="./tmp/"
    filename="google-10000-english-no-swears.txt"
    f=open(folder+filename,'r')
    #Create a simple dictonary of words
    a=f.read().splitlines()
    words=set(a)
    phase={}

    tmp_w=w
    sentence=''
    for i in k:
        for c in range(1,len(tmp_w)):
            string=w[:c]
            #print(string)
            permu=list(permutations(string, i))
            lst=set(([''.join(yup) for yup in permu]))
            for word in lst:
                if word in words:
                    print(word)
                    phase[word]=i
                    words.remove(word)
                    sentence+= word
                    #print(tmp_w)
    print(sentence)

    '''
    def get_next_word(w_r,k_r, s):
        ##Keep track of words that have been added to sentence at this recursion level and avoid repeating them

        #Base Recursion
        if len(k_r)==1:
            #Add base condition for recursion
            #Generate all permutations of w_r of length k_r.pop(0)
            for a valid permutations:
                s =s+new_word
                yield s
        else:
            loop for all permutation:
                if new_word is a valid permutation:
                    w_r_tmp=filter(w_r)
                    s_tmp=s+new_word
                    yield from get_next_word(w_r_tmp, k_r, s_tmp)

    yield from get_next_word(w,list(k),'')
    '''

descrambler('trleeohelh' , (5,5))