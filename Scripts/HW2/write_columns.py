def  write_columns(data,fname):
    '''
    Here is some sample data 
    data=[5,4,6,1,9,0,3,9,2,7,10,8,4,7,1,2,7,6,5,2,8,2,0,1,1,1,2,10,6,2]
    
    Write a function that can write the following formula to three columns to a comma-separated file:
        data_value, data_value**2, (data_value+data_value**2)/3.
    
    Here is your function signature write_columns(data,fname). 
    Your written floating-point values should be formatted to the hundreths place. 
    Your function can only accept lists of integers/floats as input. 
    Note that fname is a string and data must be a list.
    '''
    assert isinstance(data, list)
    assert isinstance(fname, str)
    for i in data:
        assert (isinstance(i,int) or isinstance(i,float))
        
    outFile = open(fname, 'w')
    for i in data:
        s="{},{},{}".format(i,i**2,(i+i**2)/3)
        outFile.write(s)
        outFile.write('\n')
    outFile.close()

