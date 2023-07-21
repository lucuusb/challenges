def fizzbuzz(n):
    _fizzbuzz = []
    for x in range(1, n+1):
        _fizzbuzz.append(x)
        if x % 3 == 0:
            _fizzbuzz[x-1] = 'Fizz'
            if x % 5 == 0:
                _fizzbuzz[x-1] += 'Buzz'
        elif x % 5 == 0:
            _fizzbuzz[x-1] = 'Buzz'

    return _fizzbuzz

print(fizzbuzz(15))
#100%
