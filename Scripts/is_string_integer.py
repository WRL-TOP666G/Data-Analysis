def is_string_integer(item):
    '''
        Write a function that takes a single string character (i.e., 'a','b','c') as input and 
        returns True or False if that character represents a valid integer in base 10.
        The function should be named is_string_integer.

        :param item: input char
        :type item: str
        :return: bool
    '''
    assert isinstance(item,str)
    assert len(item)==1
    return item.isdigit()
