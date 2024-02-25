def createFile(dirname):
    file1=open(dirname+'file1.txt','w')
    file2=open(dirname+'file2.txt','w')
    file1.write('VTU')
    file2.write("UNIVERSITY")

def mergeFiles(filename1,filename2):
    readFiles=[filename1,filename2]
    with open(dirname+'newfile.txt','w') as NFile:
        for file in readFiles:
            with open(file) as OFile:
                NFile.write(OFile.read())
                OFile.close()
            NFile.write('\n')
        NFile.close()

dirname=input('Enter the path: ')
createFile(dirname)
mergeFiles(dirname+'file1.txt',dirname+'file2.txt')