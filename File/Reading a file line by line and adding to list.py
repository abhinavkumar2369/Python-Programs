# ---------  Program to open a file & each line in a list  -----------


# ---------  Method 1  -----------

with open("file.txt",'r') as file:
    list = []
    while True:       
        line = file.readline()
        if line:
            list.append(line.strip())
        else:
            break

print(list)



# ---------- Method 2 -------------

file = open("file.txt",'r')
list_1 = []

for line in file:
    list_1.append(line.strip())

print(list_1)
file.close()
