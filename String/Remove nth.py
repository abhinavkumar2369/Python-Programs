# Question ---- 3 (a)

def removenth(s,n):
    new_str = ""
    for a in range(len(s)):
        if a==n:
            continue
        else:
            new_str += s[a]
    return new_str
    
print(removenth("MANGO",1))
print(removenth("MANGO",3))
