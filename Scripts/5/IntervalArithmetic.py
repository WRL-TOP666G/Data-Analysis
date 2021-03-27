class Interval:
    '''
        Using Python object oriented programming, write a class called Interval that represents a one-dimensional open interval on the real line. This main purpose of this class is to simplify overlapping continuous intervals. The code below should get you started but there are a lot of missing pieces that you will have to figure out.

        The API should take a pair of integers as input and respond to the + operator such that

        >>> a = Interval(1,3)
        >>> b = Interval(2,4)
        >>> c = Interval(5,10)
        >>> a + b
        Interval(1,4)
        >>> b+c
        [ Interval(2,4), Interval(5,10)]
        Note that in the case of non-overlapping intervals, the output should be a list of constituent Intervals. Keep in mind that these are open intervals. Specifically,

        >>> Interval(2,3)+Interval(1,2)
        [Interval(2,3), Interval(1,2)]
        Note that these do not produce a single interval because each interval is open (not closed). The interval endpoints can be negative also (e.g., Interval(-10,-3) is valid). The output does not have to be sorted.

        Note that you have to fill in all the functions listed (i.e., remove the pass and fill in your code).

        It's up to you to decide what each of the dunder functions means for your object. For example, you have to decide what the ordering operations for your object will be in order to accomplish the required output. If you do this right, you will have a very general solution to this problem.
    '''
    
    def __init__(self, x, y):
        assert isinstance(x,int)
        assert isinstance(y,int)
        assert x<y
        self.x = x
        self.y = y
        
    def __str__(self):
        return "[Interval({},{})]".format(self.x, self.y)
    
    __repr__ = __str__
    
    
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y

    def __lt__(self,other):
        return self.y<other.x

    def __gt__(self,other):
        return self.x>other.y

    def __ge__(self,other):
        return self.x>=other.y

    def __le__(self,other):
        return self.y<=other.x

    def __add__(self,other):
        if self.intersected(other):
            return "[Interval({},{})]".format(min(self.x,other.x),max(self.y,other.y))
        else:
            return "[Interval({},{}), Interval({},{})]".format(self.x,self.y,other.x,other.y)
        
    
    def intersected(self,other):
        if other.x<=self.x:
            if other.y>self.x:
                return True
            else:
                return False
        elif self.x<other.x and other.x<self.y:
            return True
        else:
            return False
