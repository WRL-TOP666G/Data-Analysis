def compute_average_word_length(instring, unique=False):
    '''
        Write a compute_average_word_length(instring,unique=False) function 
        to compute the average length of the words in the input string (instring). 
        If the unique option is True, then exclude duplicated words. 
        For example, in the example input text above, 
        the word the should be counted exactly once for the average word length if unique=True. 
        Note that the words are case sensitive. 
        Remember to carefully validate your inputs using assert statements.

        :param1 instring: input non-digit
        :type1 instring: string

        :param2 unique: input True or False
        :type2 instring: boolean

        :return: float

        - ///punctuation does not count for word length(ignored) . "pi." has a length of 2
        - ////output is not rounded (keep it as the unrounded float)
        - ///"long-term" counts as 1 word (length 8)
        - ///a string containing integers is not allowed (via assertion)
        - suppose you have "them," and "them"  . 
          If unique is True, one of the "them"s will be removed because punctuation is ignored 
          (the comma in this example)
    '''
    
    for c in instring:
        assert not c.isdigit()
    assert len(instring.split())!=0
    s=instring.split()
    sum=0.0
    if unique:
        myset=set(s)
        for word in myset:
            sum+=len(word)
            print(word)
        return float(sum)/float(len(myset))
    else: 
        for word in s:
            sum+=len(word)
            print(word)
        return float(sum)/float(len(s))


