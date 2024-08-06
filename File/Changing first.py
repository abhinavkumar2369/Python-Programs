# Change Character with # in the file

def changecharacter(file,char):
    import os
    f = open(file,'r')
    g = open('temp.txt','w')
    for line in f:
        line = line.replace(char,"#")
        g.write(line)
    f.close()
    g.close()
    os.remove(file)
    os.rename("temp.txt",file)


changecharacter("old_file.txt","T")