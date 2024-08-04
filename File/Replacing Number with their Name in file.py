file = open("example.txt",'r+')

l = ['0','1','2','3','4','5','6','7','8','9']
name = ['zero','one','two','three','four','five','six','seven','eight','nine']

lines = file.readlines()
new_lines = []

for a in lines:
    str = ''
    for b in a:
        if b in l:
            str += name[l.index(b)]
        else:
            str += b
    new_lines.append(str)

file.seek(0)
file.writelines(new_lines)

file.close()