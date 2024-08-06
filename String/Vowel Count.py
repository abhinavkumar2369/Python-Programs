# Program to count no of vowel and returns its value

def vowel_count(s):
    count = 0
    vowels = ['a','e','i','o','u']
    for a in s:
        if a.lower() in vowels:
            count += 1
    return count


print(vowel_count("Abhinav"))
# returns 3