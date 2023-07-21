def perimeter(n):
    num, sequence = 0, 1
    perimeter = 1
    for _ in range(n):
        num, sequence = sequence, num + sequence
        perimeter += sequence
    return 4 * perimeter

#100%. Fast
print(perimeter(7))
