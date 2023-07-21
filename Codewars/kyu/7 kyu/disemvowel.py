def disemvowel(string_):
    for v in 'aeiouAEIOU':
        string_ = string_.replace(v, '')
    return string_

#100%
print(disemvowel('Not a vowel'))