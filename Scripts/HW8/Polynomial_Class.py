class Polynomial:
    '''
        Polynomial Class
        Create a Python class that can implement a univariate polynomial with degree 
        at least one (Polynomial) over the field of integers (only!) with the following operations and interfaces.

            √ >>> p=Polynomial({0:8,1:2,3:4}) # keys are powers, values are coefficients
            √ >>> q=Polynomial({0:8,1:2,2:8,4:4})
            √ >>> repr(p)
                8 + 2 x + 4 x^(3)
            √ >>> p*3 # integer multiply
                24 + 6 x + 12 x^(3)
            √ >>> 3*p # multiplication is commutative!
                24 + 6 x + 12 x^(3)
            √ >>> p+q # add two polynomials
                16 + 4 x + 8 x^(2) + 4 x^(3) + 4 x^(4)
            √ >>> p*4 + 5 - 3*p - 1 # compose operations and add/subtract constants
                12 + 2 x + 4 x^(3)
            √ >>> type(p-p) # zero requires special handling but is still a Polynomial
                Polynomial
            √ >>> p*q # polynomial by polynomial multiplication works as usual
                64 + 32 x + 68 x^(2) + 48 x^(3) + 40 x^(4) + 40 x^(5) + 16 x^(7)
            √ >>> p.subs(10) # substitute in integers and evaluate
                4028
            √ >>> (p-p) == 0
                True
            √ >>> p == q
                False
            √ >>> p=Polynomial({0:8,1:0,3:4}) # keys are powers, values are coefficients
            √ >>> repr(p)
                '8 + 4 x^(3)'
            √ >>> p = Polynomial({2:1,0:-1})
            √ >>> q = Polynomial({1:1,0:-1})
            √ >>> p/q
                1 + x
            √ >>> p  / Polynomial({1:1,0:-3}) # raises NotImplementedError
    '''
    def __init__(self,dic):
        assert isinstance(dic,dict)
        tmp=dic
        for key, value in dic.items():
            assert isinstance(key, int) and isinstance(value, int)
        for key in list(tmp):
            if tmp[key]==0 and key!=0:
                del tmp[key]
        self.dic = dict(sorted(tmp.items()))
        
    def __str__(self):
        s=''
        for key, value in self.dic.items():
            if value==0:
                continue
            if key==0:
                s+='{}'.format(value)
            elif key==1:
                if value>0:
                    s+=' + '
                else: 
                    s+=' - '
                    
                if value==1:
                    s+='x'
                else: 
                    s+='{} x'.format(abs(value))
            else:
                if value>0:
                    s+=' + '
                else: 
                    s+=' - '
                    
                if value==1:
                    s+=' x^({})'.format(key)
                else: 
                    s+='{} x^({})'.format(abs(value),key)
        if s=='':
            return '0'
        return s

    
    __repr__ = __str__
     
    def __pos__(self):
        return Polynomial(self)
    
    def __neg__(self):
        tmp={}
        for key, value in self.dic.items():
            tmp[key]=-value
        return Polynomial(tmp)
    
            
    def __add__(self, other):
        if type(other)==int:
            self.dic[0]+=other
            return Polynomial(self.dic)
        tmp={}
        dicKey=list(self.dic)
        otherKey=list(other.dic)
        i=0
        j=0
        while i<len(dicKey) and j<len(otherKey):
            if dicKey[i]==otherKey[j]:
                tmp[dicKey[i]]=self.dic[dicKey[i]]+other.dic[otherKey[j]]
                i+=1
                j+=1
            elif dicKey[i]<otherKey[j]:
                tmp[dicKey[i]]=self.dic[dicKey[i]]
                i+=1
            elif dicKey[i]>otherKey[j]:
                tmp[otherKey[j]]=other.dic[otherKey[j]]
                j+=1
        
        while i<len(dicKey):
                tmp[dicKey[i]]=self.dic[dicKey[i]]
                i+=1
                
        while j<len(otherKey):
                tmp[otherKey[j]]=other.dic[otherKey[j]]
                j+=1
        
        return Polynomial(tmp)
    
    def __radd__(self, other): 
        return self.__add__(other)
            
    def __sub__(self, other): 
        tmp={}
        if type(other)==int:
            self.dic[0]-=other
            return Polynomial(self.dic)
        dicKey=list(self.dic)
        otherKey=list(other.dic)
        i=0
        j=0
        while i<len(dicKey) and j<len(otherKey):
            if dicKey[i]==otherKey[j]:
                tmp[dicKey[i]]=self.dic[dicKey[i]]-other.dic[otherKey[j]]
                i+=1
                j+=1
            elif dicKey[i]<otherKey[j]:
                tmp[dicKey[i]]=self.dic[dicKey[i]]
                i+=1
            elif dicKey[i]>otherKey[j]:
                tmp[otherKey[j]]=-other.dic[otherKey[j]]
                j+=1
                
        while i<len(dicKey):
                tmp[dicKey[i]]=self.dic[dicKey[i]]
                i+=1
                
        while j<len(otherKey):
                tmp[otherKey[j]]=-other.dic[otherKey[j]]
                j+=1
        
        return Polynomial(tmp)
    
    def __rsub__(self, other): 
        return self.__sub__(other)
    
    def __mul__(self, other):
        tmp={}
        if type(other) == int:
            for key, value in self.dic.items():
                tmp[key]=value*other
        else: 
            for key_i, value_i in self.dic.items():
                for key_j, value_j in other.dic.items():
                    if not tmp.get(key_i+key_j):
                        tmp[key_i+key_j]=value_i*value_j
                    else: 
                        tmp[key_i+key_j]+=value_i*value_j
                
        return Polynomial(tmp)
            
    def __rmul__(self, other):
        return self.__mul__(other)
    
    
    
    def __truediv__(self, other):
        if type(other)==int:
            for key, value in self.dic.items():
                self.dic[key]=self.dic[key]//other
            return self.dic
        tmp={}
        tmpDic = dict(sorted(self.dic.items()))
        other.dic = dict(sorted(other.dic.items()))
        
        selfDeg=max(tmpDic.keys())
        otherDeg=max(other.dic.keys())
        while selfDeg>=otherDeg and tmpDic and other.dic:
            selfDeg=max(tmpDic.keys())
            otherDeg=max(other.dic.keys())
            
            selfCoff=tmpDic[selfDeg]
            otherCoff=other.dic[otherDeg]
            
            if otherDeg>selfDeg:
                break
            else:
                for key in reversed(list(other.dic)):
                    if not tmpDic.get(key+(selfDeg-otherDeg)):
                        tmpDic[key+(selfDeg-otherDeg)]=-other.dic[key]*(selfCoff//otherCoff)
                    else: 
                        tmpDic[key+(selfDeg-otherDeg)]-=other.dic[key]*(selfCoff//otherCoff)
        
                    for k in reversed(list(tmpDic)): 
                        if tmpDic[k]==0:
                            del tmpDic[k]
            tmp[selfDeg-otherDeg]=(selfCoff//otherCoff)
        if len(tmpDic)!=0:
            raise NotImplementedError
        return Polynomial(tmp)
    
    def __eq__(self, other):
        if type(other)!=Polynomial:
            other={0:other}
            other=Polynomial(other)
        return (self.dic) == (other.dic)
    
    
    def subs(self, args):
        assert isinstance(args,int)
        res=0
        for key, value in self.dic.items():
            res+=value*(args**key)
        return res