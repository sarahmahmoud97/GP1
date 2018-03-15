import nltk
import os
import glob
path= r"D:\GraduationProject1\datasets\arabicPoetries\الخنساء\test"
os.chdir(path)
for infile in glob.glob( os.path.join(path, '*.txt') ):
    f=open(os.path.join(path, infile),encoding="utf8")
    lines=f.readlines()
    print(len(lines))
    outfile = open(( infile.rsplit( ".", 1 )[ 0 ] ) + ".txt",'w',encoding="utf8" ) 
    for i in range(0,len(lines)):
        if (i%2!=0):
            outfile.write(lines[i]+"*")
            outfile.write("\n")
        else:
            outfile.write(lines[i])
    outfile.close()
