# Write a Python function that accepts a list of numbers and returns a new list with only the unique elements, preserving their original order.

def unique_element_list(list):
    new_list = []
    for element in list:
        if new_list.count(element) == 0:
            new_list.append(element)
    return new_list


# Example
list_1 = [1,2,3,1,4,2,5,6,5,6]

# List with non Unique element
print(unique_element_list(list_1))

# Output
[1,2,3,4,5,6]