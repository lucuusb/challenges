"""
Version 1
def dirReduc(arr):
    redundancies = [
        ("NORTH", "SOUTH"),
        ("SOUTH", "NORTH"),
        ("WEST", "EAST"),
        ("EAST", "WEST"),
    ]
    optimal = False
    i = 0
    while not optimal:
        if i < len(arr) > 1:
            if (arr[i], arr[i + 1]) in redundancies:
                del arr[i]
                del arr[i]
                i = 0
            elif i + 2 == len(arr):
                optimal = True
            else:
                i += 1
        else:
            optimal = True
    return arr
"""


# Version 1.5
def dirReduc(arr):
    redundancies = [
        ("NORTH", "SOUTH"),
        ("SOUTH", "NORTH"),
        ("WEST", "EAST"),
        ("EAST", "WEST"),
    ]
    optimal = False
    while not optimal:
        i = 0
        changing = False
        while i + 1 < len(arr):
            if (arr[i], arr[i + 1]) in redundancies:
                del arr[i]
                del arr[i]
                changing = True
            i += 1
        if not changing:
            optimal = True
    return arr

# 100%
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
