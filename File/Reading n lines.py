

def reading_n_line(n):
    with open("file.txt",'r') as file:
        count = 0
        while count<n:
            line = file.readline()
            print(line.strip())
            count = count + 1

# -------------- Reading n lines ---------
reading_n_line(2)