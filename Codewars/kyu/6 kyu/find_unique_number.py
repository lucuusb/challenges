def find_uniq(arr):
    arr.sort()
    for i, n in enumerate(arr):
        if i == 0:
            if arr[i+1] != n:
                break
        elif i+1 == len(arr):
            if arr[i-1] != n:
                break
        elif arr[i-1] != n and arr[i+1] != n:
            break
    return n

find_uniq([1, 2, 1])
#100%
#Tip: The 'set' built-in data type does not allow duplicate ellements.