# Write a program that counts the number of occurrences of a specific character in a string.

def character_occurrence(string,element):
    count = 0
    for a in string:
        if a == element:
            count += 1
    return count

string = "Hello I am ShyDuck"
count = character_occurrence(string)

print(count)