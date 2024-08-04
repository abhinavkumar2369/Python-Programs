## Lists

- Write a program that removes all duplicate items from a list.
```py
def unique_element_list(list):
    new_list = []
    for element in list:
        if new_list.count(element) == 0:
            new_list.append(element)
    return new_list

list_1 = [1,2,3,1,4,2,5,6,5,6]
print(unique_element_list(list_1))

# Output ---> [1,2,3,4,5,6]
```


- Write a program that sorts a list of numbers in descending order.
```py
def descending_order(list):
    list.reverse()
    return list

list = [10,3,4,16,1]
print(descending_order(list))
```


- Write a program that finds the second-largest number in a list.
```py
def second_largest_element(list):
    if len(list)<2:
        print("Less than 2 Elements")
    else:
        list.sort(reverse = True)
        print(list[1])

l = [1,2,7,3,4,5,8]
m = []

second_largest_element(l)
second_largest_element(m)
```
