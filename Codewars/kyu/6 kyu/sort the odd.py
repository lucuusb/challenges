import operator

#incomplete
def sort_odds_in_array(source_array):
    sorted_array = []
    odd_array = []
    even_indexes = {}
    for n in source_array:
        if n % 2 != 0:
            odd_array.append(n)
        else:
            even_indexes += source_array.index(n), n
    sorted_array = sorted(odd_array)
    for i in even_indexes:
        sorted_array[operator.getitem(even_indexes[0])] = operator.getitem(even_indexes[1])
        operator.getitem(even_indexes[1])

sort_odds_in_array([5, 8, 6, 3, 4])
#                  [3, 8, 6, 5, 4]