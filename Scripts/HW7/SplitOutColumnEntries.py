def split_count(x):
    '''
        Split out column entries
        Load following survey data into a Pandas dataframe called x and note that the top part of the Is there anything in particular you want to use Python for? column looks like the following,

        Is there anything in particular you want to use Python for?
        ID	
        3931	Data extraction and processing, Data analytics...
        4205	Data extraction and processing
        3669	Data analytics, Machine learning, Statistical ...
        1452	Data extraction and processing, Data analytics...
        2968	Numerical processing, Data analytics, Machine ...
        The problem with this column is that there are multiple comma-separated values in it. Please write a Python function called split_count that can take this column as input and output the following Pandas dataframe.

        count
        All of the above	1
        Computer vision	1
        Image Processing	1
        Computer vision/image processing	1
        As a general skill	1
        scripting seems desirable for many jobs	1
        not sure	1
        Computer Vision	1
        EDA tools	1
        Web development	104
        Numerical processing	173
        Scientific visualization	198
        Statistical analysis	222
        Data extraction and processing	291
        Data analytics	351
        Machine learning	381
        Here is the function signature: split_count(x) where x is a pd.Series object and it returns a pd.DataFrame object.

    '''
    import pandas as pd
    assert isinstance(x,pd.Series)
    dic={}
    for string in x:
        assert isinstance(string,str)
        l=string.split(",")
        for s in l: 
            #print(s)
            assert isinstance(s,str)
            s=s.strip()
            if s not in dic:
                dic.update({s:1})
            else:
                dic[s]+=1
    dic=dict(sorted(dic.items(), key=lambda item: item[1]))
    #dic = OrderedDict(sorted(dic.items(), key=lambda t:t[1]))
    #ans=pd.DataFrame(dic.items(), columns=['', 'count'])
    ans=pd.DataFrame( dic.values(),index=dic.keys(), columns=[ 'count'])
    #ans=ans.sort_values(['count'], axis=1, ascending=True)
    assert isinstance(ans,pd.DataFrame)
    return ans
