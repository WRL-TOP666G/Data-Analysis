def write_chunks_of_five(words,fname): 
    '''
    Using corpus of 10,000 common English words, 
    create a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line. 
    Here are the first 10 lines of ouptut corresponding to the above sample corpus:

        the of and to a
        in for is on that
        by this with i you
        it not or be are
        from at as your all
        have new more an was
        we will home can us
        about if page my has
        search free but our one
        other do no information time

        .
    If the last group has less than five at the end, just write out the last group. Here is your function signature: 
    write_chunks_of_five(words,fname). 
    The words is a list of words from the above corpus and fname is the output filename string.
    '''
    assert isinstance(words, list)
    assert isinstance(fname, str)
    for i in words:
        assert isinstance(i,str)

    outFile = open(fname, 'w')
    for i in range(len(words)):
        if i%5==0:
            s=''
        s+=words[i]
        if (i+1)%5==0 or i==len(words)-1:
            outFile.write(s)
            if i!=len(words)-1:
                outFile.write('\n')
        else: 
            s+=' '
        
    outFile.close()
    