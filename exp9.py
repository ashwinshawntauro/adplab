def mergeFiles(filename1,filename2):
    readFiles=[filename1,filename2]
    with open(dirname+'newfile.txt','w') as NewFile:
        for oldFiles in readFiles:
            with open(oldFiles) as inputFile:
                NewFile.write(inputFile.read())
                inputFile.close()
            NewFile.write('\n')
        NewFile.close()

def createFile(dirname):
    file1=open(dirname+'file1.txt','w')
    file2=open(dirname+'file2.txt','w')
    file1.write("VTU")
    file2.write("University")

print("File Management")
dirname=input('Enter dirname: ')
createFile(dirname)
mergeFiles(dirname+'file1.txt',dirname+'file2.txt')
 