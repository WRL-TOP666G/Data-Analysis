def add_month_yr(x):
    import pandas as pd
    assert isinstance(x,pd.DataFrame)
    date=x['Timestamp']
    date = pd.to_datetime(date)
    result=date.dt.strftime('%b-%Y')
    x['month-yr']=result
    return(x)

def fix_categorical(x):
    '''
        The problem with our previous result is that the order is wrong. 
        Convert the month-yr column dtype to 
        a Pandas CategoricalDtype with the correct order. 
        You should be able to reproduce the following statement,

        >>> x.groupby('month-yr')['Timestamp']
        .count().to_frame().sort_index() 

        Timestamp
        month-yr	
        Sep-2017	74
        Jan-2018	148
        Feb-2018	2
        Mar-2018	41
        Apr-2018	28
        Sep-2018	130
        Oct-2018	6
        Jan-2019	57

        Note that the groupby is now sorted correctly. 
        Your function signature is fix_categorical(x). 
        It should take the month-yr dataframe column and then 
        return the same dataframe with 
        an updated column of CategoricalDtype that 
        does the sorting as described. 
        Remember to include your add_month_year code from the previous part, 
        as your new function needs the output from it.

        Here is your function signature fix_categorical(x) 
        where x is a pd.DataFrame with the required "month-yr" column 
        and output is a pd.DataFrame with the "month-yr" column 
        having the categorical dtype.
    '''
    import pandas as pd
    assert isinstance(x,pd.DataFrame)
    myList=[]
    for i in range(len(x)):
        if x['month-yr'][i] not in myList:
            myList.append(x['month-yr'][i])
    myList
    cat_type = pd.api.types.CategoricalDtype(categories=myList, ordered=True)
    x['month-yr'] = x['month-yr'].astype(cat_type)
    return x
