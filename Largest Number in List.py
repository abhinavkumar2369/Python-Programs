# Write a function that takes a list of numbers and returns the largest number.

def largest_number_in_list(list):
    if len(list)<1:
        print("Empty List")
        return
    else:
        largest = list[0]
        for a in list:
            if a>largest:
                largest = a
        return largest

# Initialize
list_1 = [10,24,9,5,31,20]
list_2 = []


print(largest_number_in_list(list_1))
# Return 31

print(largest_number_in_list(list_2))
# Print message ----> Empty List
# returns None