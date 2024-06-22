def remove_vowel(string):
    new_string = ''
    vowel = ['a','e','i','o','u']
    for a in string:
        if a.lower() in vowel:
            continue
        else:
            new_string += a
    return new_string

a = 'Hello I am Shy Duck'
print(remove_vowel(a))