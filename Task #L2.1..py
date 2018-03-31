def union(*args):
    '''This function returns
    union of any iteriable objects'''
    s = []
    for arg in args:
        for i in arg:
            s.append(i)
    s = set(s)
    return list(s)

def intersect(*args):
    '''This function returns
    intersect of any iteriable objects'''
    s = []
    l = []
    for arg in args:
        for i in arg:
            s.append(i)
    for j in s:
        if s.count(j) >= len(args):
            l.append(j)
    return list(l)

print(intersect("avsds", "sdsaads", "dsaad", "afqfdsafdsa"))