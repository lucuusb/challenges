def vowel_counter(string):
    vowels = 'aeiou'
    counter = 0
    for v in vowels:
        counter += string.count(v)
    return counter

texto = vowel_counter('umuarama')
print(texto)

#100%
'''Optimized version:
def vowel_counter(string):
    return sum(v in 'aeiou' for v in string)
'''