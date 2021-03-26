def split_by_n(fname,n=3):
   '''
   Split files into sub files of near same size
   fname : Input file name
   n is the number of segments
   '''
   import os 
   assert isinstance(n,int) and n>0
   assert isinstance(fname,str) and len(fname)>0

   fileSize=os.path.getsize(fname)
   with open(fname, 'r') as file:
      line=file.readline()
      setList=[]
      while line:
         setList.append(line)
         line=file.readline()
   chunkSize=fileSize/n
   sizeKeeper=0
   lineNum=0
   for num in range(n):
      newLine=fname+'_'+str(num).zfill(3)+'.txt'
      with open(newLine, 'wt') as file:
         while (sizeKeeper + len(setList[lineNum])) <= (num+1) * chunkSize:
                file.write(setList[lineNum])
                sizeKeeper += len(setList[lineNum])
                lineNum += 1
                if lineNum >= len(setList):
                    break

