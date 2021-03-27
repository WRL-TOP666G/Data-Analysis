def add_month_yr(x):
    import pandas as pd
    assert isinstance(x,pd.DataFrame)
    date=x['Timestamp']
    date = pd.to_datetime(date)
    result=date.dt.strftime('%b-%Y')
    x['month-yr']=result
    return(x)


def count_month_yr(x):
    '''
    Write a function count_month_yr to create the following dataframe using your new column month-yr,

    Timestamp
    month-yr	
    Apr-2018	28
    Feb-2018	2
    Jan-2018	148
    Jan-2019	57
    Mar-2018	41
    Oct-2018	6
    Sep-2017	74
    Sep-2018	130
    Notice that the order of the dates is incorrect. 
    We will fix that later. 
    Remember to include your add_month_yr code from the previous part, 
    as your new function needs the output from it.

    Here is the function signature: 
    count_month_yr(x) where x is 
    a pd.DataFrame that returns a pd.DataFrame.
    '''
    import pandas as pd
    assert isinstance(x,pd.DataFrame)
    x=add_month_yr(x)
    dic={}
    for i in range(len(x)):
        s=x['month-yr'][i]
        if s not in dic:
            dic.update({s:1})
        else:
            dic[s]+=1
    ans=pd.DataFrame( dic.values(),index=dic.keys(), columns=[ 'Timestamp'])
    return ans
