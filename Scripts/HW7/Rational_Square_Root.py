class Rational:
    '''
        Implement a class of rational numbers (ratio of integers) with the following interfaces and behaviours

      √  >>> r = Rational(3,4) √
      √  >>> repr(r) √
        '3/4'
      √  >>> -1/r
        -4/3
      √  >>> float(-1/r) √
        -1.3333333333333333
      √  >>> int(r) √
        0
      √  >>> int(Rational(10,3)) √
        3
      √  >>> Rational(10,3) * Rational(101,8) - Rational(11,8) √
        977/24
      √ >>> sorted([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)])
        [1/100, 9/8, 10/3, 10]
      √  >>> Rational(100,10) √
        10
      √ >>> -Rational(12345,128191) + Rational(101,103) * 30/ 44
        166235595/290480806
    '''

    def __init__(self,numer,denom):
        assert isinstance(numer,int)
        assert isinstance(denom,int) and denom!=0
        def gcd(m, n):
            while m % n != 0:
                old_m = m
                old_n = n
                m = old_n
                n = old_m % old_n
            return n
        common = gcd(numer,denom)
        self.numer = numer//common
        self.denom = denom//common

    def __str__(self):
        if self.denom==1:
            return str(self.numer)
        return '%s/%s' % (self.numer,self.denom)
    
    __repr__ = __str__
    
    def __int__(self):
        return int(self.numer/self.denom)
    
    def __float__(self):
        return self.numer/self.denom
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Rational(-self.numer,self.denom)
    
    
    def __add__(self, other):
        if type(other)==Rational:
            return Rational(self.numer * other.denom + other.numer * self.denom, 
                            self.denom * other.denom)
        if type(other)==int:
            return Rational(self.numer + other*self.denom, 
                            self.denom )
        else: 
            raise('Error')
    
    def __radd__(self, other):
        return Rational(self.numer + other*self.denom, self.denom)
    
    
    def __sub__(self, other): 
        return Rational(self.numer * other.denom - other.numer * self.denom,
                        self.denom * other.denom)
    
    def __rsub__(self, other): 
        return Rational(other * self.denom - self.numer , self.denom )
    

    def __truediv__(self, other):
        new= Rational(self.numer, self.denom*other)
        return new
    
    def __rtruediv__(self,other):
        new = Rational(other*self.denom, self.numer)
        return new
    
    def __mul__(self, param_Rational):
        if type(param_Rational) == int:
            param_Rational = Rational(param_Rational,1)
        if type(param_Rational) == Rational:
            new_numerator = self.numer * param_Rational.numer
            new_denominator = self.denom * param_Rational.denom
            return Rational(new_numerator, new_denominator)
        else:
            raise("type error")
    
    def __rmul__(self, param):
        return self.__mul__(param)
    
    def __eq__(self, other):
        return (self.numer/self.denom) == (other.numer/other.denom)

    def __lt__(self, other):
        return (self.numer/self.denom) < (other.numer/other.denom)

    def __le__(self, other):
        return (self.numer/self.denom) <= (other.numer/other.denom)

    def __gt__(self, other):
        return (self.numer/self.denom) >(other.numer/other.denom)

    def __ge__(self, other):
        return (self.numer/self.denom) >= (other.numer/other.denom)
    
    def __abs__(self):
        return abs(self.numer/self.denom)

def square_root_rational(x,abs_tol=Rational(1,1000)):
    '''
        Using your Rational class for representing rational numbers, 
        write a function square_root_rational which takes 
        an input rational number x and returns the square root of x to absolute precision abs_tol. 
        Your function should return a Rational number instance as output. Here is an example,

        >>> square_root_rational(Rational(1112,3),abs_tol=Rational(1,1000)) 
        # output is `Rational` instance 10093849/524288

        Here is your function signature: square_root_rational(x,abs_tol=Rational(1,1000)).

        Hint: Use the bisection algorithm to compute the square root.
    '''
    assert isinstance(x, Rational)
    assert isinstance(abs_tol, Rational)
    num=float(x)**(1/2)
    i=0
    numer=1
    denum=1
    while abs(numer/denum-num)>=float(abs_tol):
        numer=int(num*(10**i))
        denum=(10**i)
        i+=1
    r=Rational(numer,denum)
    return r
