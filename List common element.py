# Write a function that takes two lists and returns a new list containing the elements that are in both lists (intersection).

def list_common_element(l1,l2):
    new_list = []
    for a in l1:
        if a in l2:
            if new_list.count(a):
                pass
            else:
                new_list.append(a)
    return new_list


a = [1,2,3,4,5]
b = [2,5,7,1,5,3]


print(list_common_element(a,b))