def split_by_n(fname,n=3):
   '''
        You have a file that needs to be divided into n chunks. While it would be straightforward to split the file into equal-bytes sizes and then write those chunks to file, you cannot write any incomplete lines to the files. This means that all of the n files that you create must have no truncated lines. If a split of a certain byte-size would result in a truncated line, then you can back off and only write the previous complete line. You can save the rest of it for the next chunk.

        You can download Metamorphosis, by Franz Kafka as the sample text. The file is of size 139055 bytes. Splitting into three pieces gives the following files and their respective sizes:

        size    filename
        46310    pg5200.txt_00.txt
        46334    pg5200.txt_01.txt
        46411    pg5200.txt_02.txt
        The last line of the pg5200.txt_00.txt is the following:

        her, she hurried out again and even turned the key in the lock so

        The last line of the pg5200.txt_01.txt is the following:

        there.  He, fortunately, would usually see no more than the object

        As a final hint, splitting the same file into eight parts gives the following:

        size    filename
        17321    pg5200.txt_00.txt
        17376    pg5200.txt_01.txt
        17409    pg5200.txt_02.txt
        17354    pg5200.txt_03.txt
        17445    pg5200.txt_04.txt
        17332    pg5200.txt_05.txt
        17381    pg5200.txt_06.txt
        17437    pg5200.txt_07.txt
        You should think about making your file sizes as uniform as possible. Otherwise, for a very long file, the last file may be inordinately large, as compared to the others. Your algorithm should pass through the file exactly once. If possible, you also want to minimize how much you move the file pointer around in the file. You should ensure that your code produces the file sizes that are indicated for each of the cases shown above.

        Hint: Use wb as the file write mode.
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

