def tribonacci(signature, n):
    for i in range(n):
        signature.append(sum(signature[i:i+3]))
    return signature[:n]

print(tribonacci([1, 1, 1], 10))
#100%
#It's been suggested not to change the original signature during execution