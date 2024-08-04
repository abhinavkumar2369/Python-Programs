# Program to print the second largest element in the list

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