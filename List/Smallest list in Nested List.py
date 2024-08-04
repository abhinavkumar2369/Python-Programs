def smallest_nested_list(l):
    if len(l)==0:
        return []
    sl = l[0]
    for a in l:
        if len(sl)<len(a):
            sl = a
    return sl
