def add_month_yr(x):
    '''
        Add a new column using Timestamp column
        Using the same survey dataframe from before, 
        create a dataframe column month-yr with ID as row-index like 
        the following,

        month-yr
        ID	
        3931	Sep-2017
        4205	Sep-2017
        ...	...
        2524	Jan-2019
        Note that each of the entries is a string. 
        That is, given that your original survey dataframe is x, 
        you should be able to produce the output above from

        >>> x['month-yr'] 
        Your function add_month_yr(x) should take in the x survey 
        dataframe and then output the same dataframe with 
        a new month-yr column.

        Here is the function signature: add_month_yr(x) where 
        x is a pd.DataFrame and returns the same pd.DataFrame 
        with the new column. This means all you have to do 
        is take the input dataframe and add a single column to it.

        HINT:
        You do not need to reindex the dataframe. 
        Just add the specified column.
    '''
    import pandas as pd
    assert isinstance(x,pd.DataFrame)
    date=x['Timestamp']
    date = pd.to_datetime(date)
    result=date.dt.strftime('%b-%Y')
    x['month-yr']=result
    return(x)