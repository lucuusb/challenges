import copy


def find_uniq(arr):
    strings = copy.copy(arr)
    for elem in arr:
        strings.remove(elem)
        for s in elem:
            if s not in strings:
                break
            else:
                continue
        print(s)
    return s
#Unfinished. Maybe sets and the 'in' keyword?
print(find_uniq(["abc", "acb", "bca", "cba", "gg"]))
