def  get_average_word_length(words):
    '''
        Download this corpus of 10,000 common English words and write the following functions given a list of words:

        Compute the average length of the words (get_average_word_length(words))
        What is the longest word (get_longest_word(words))?
        What is the longest word that starts with a single letter (get_longest_words_startswith(words,start))
        What is the most common starting letter (get_most_common_start(words))?
        What is the most common ending letter (get_most_common_end(words))
        For testing you can use this bit of code to download the words from the corpus:

        from urllib.request import urlopen
        u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
        response = urlopen(u)
        words = [i.strip().decode('utf8') for i in response.readlines()]

    '''
    #assert
    assert isinstance(words,list)
    assert len(words)>0
    for i in words:
        assert isinstance(i,str)
        assert len(i)>0
        
    summary=0
    for i in words:
        summary+=len(i)
    return (summary/len(words))


def get_longest_word(words):
    assert isinstance(words,list)
    assert len(words)>0
    for i in words:
        assert isinstance(i,str)
        assert len(i)>0

    max=0
    ans=''
    for i in words:
        if len(i)>max:
            max=len(i)
            ans=i
    return ans

def get_longest_words_startswith(words,start):
    assert isinstance(words,list)
    assert len(words)>0
    for i in words:
        assert isinstance(i,str)
        assert len(i)>0
    assert isinstance(start, str)
    assert len(start)==1
    
    max=0
    ans=''
    for i in words:
        if i[:len(start)]==start and len(i)>max:
            max=len(i)
            ans=i
    return ans
    


def get_most_common_start(words):
    from collections import defaultdict
    assert isinstance(words,list)
    assert len(words)>0
    for i in words:
        assert isinstance(i,str)
        assert len(i)>0
    
    d=defaultdict(list)
    max=0
    ans=''
    for i in words:
        d[i[0]].append(i)
        
    for i in d:
        if len(d[i])>max:
            max=len(d[i])
            ans=i
    return ans



def get_most_common_end(words):
    from collections import defaultdict
    assert isinstance(words,list)
    assert len(words)>0
    for i in words:
        assert isinstance(i,str)
        assert len(i)>0
    
    d=defaultdict(list)
    max=0
    for i in words:
        d[i[-1]].append(i)
        
    for i in d:
        if len(d[i])>max:
            max=len(d[i])
            ans=i
    return ans
