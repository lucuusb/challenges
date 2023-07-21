from collections import deque


def queue_time(customers, n):
    queue = deque(customers)
    tills = [0]*n
    while len(queue) > 0:
        free_till = tills.index(min(tills))
        tills[free_till] += queue.popleft()
    return max(tills)

#100%
print(queue_time([5, 4, 3], 1))  # should return 12
print(queue_time([2, 3, 6, 8], 2))  # should return 11
print(queue_time([3, 7, 4, 2, 10], 3))  # should return 14
print(queue_time([5, 2, 6, 4, 5, 7, 1, 8, 3, 4, 5, 8, 1, 3], 3))  # should return 23
#                 1  2  3  2  1  3  2  2  1  3  1  2  3  3
""" T1 T2 T3
    5  2  6
    5  4  7
    3  1  4
    5  8  1
       8  3
T: 18 23 21
"""
# T1: 5+5+3+5=18
# T2: 2+4+1+8+8=23
# T3: 6+7+4+1+3=21
