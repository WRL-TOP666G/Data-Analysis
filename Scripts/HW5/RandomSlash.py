def gen_rand_slash(m=6,n=6,direction='back'):
    import numpy as np
    import random
    
    assert isinstance(m,int) and m>1
    assert isinstance(n,int) and n>1
    assert isinstance(direction,str) and len(direction)>0

    arr=np.zeros((n,m))
    num=random.randint(0,1)
    if direction=='back':
        while True:
            arr=np.zeros((n,m))
            num=random.randint(0,1)
            num_m=random.randint(0,m-1)
            num_n=random.randint(0,n-1)
            
            if num%2==0:
                i=num_m
                j=num_n
                while i>=0 and j>=0:
                    arr[i][j]=1
                    i-=1
                    j-=1
            if num%2==1:
                i=num_m
                j=num_n
                while i<m and j<n:
                    arr[i][j]=1
                    i+=1
                    j+=1
            count=0
            for i in range(m):
                for j in range(n):
                    if arr[i][j]==1:
                        count+=1
            if count==1:
                continue
            else:
                break;
    
    elif direction=='forward':
        
        while True:
            arr=np.zeros((n,m))
            num=random.randint(0,1)
            num_m=random.randint(0,m-1)
            num_n=random.randint(0,n-1)
            if num%2==0:
                i=num_m
                j=num_n
                while i>=0 and j<n:
                    arr[i][j]=1
                    i-=1
                    j+=1
            if num%2==1:
                i=num_m
                j=num_n
                while i<m and j>=0:
                    arr[i][j]=1
                    i+=1
                    j-=1
            count=0
            for i in range(m):
                for j in range(n):
                    if arr[i][j]==1:
                        count+=1
            if count==1:
                continue
            else:
                break;
    
    return arr

