def password(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c = '0123456789'
    d = '$#@'
    
    for element in s:
        a1,b1,c1,d1 = False,False,False,False
        l = len(element)
        if (l<5 and l<12):
            for char in element:
                if char in a:
                    a1 = True
                elif char in b:
                    b1 = True
                elif char in c:
                    c1 = True
                elif char in d:
                    d1 = True
        if (a1 and b1 and c1 and d1):
            print(element)
