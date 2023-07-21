def duplicate_count(text):
    lowertext = text.lower()
    s = {char for char in lowertext if lowertext.count(char) > 1}#Inefficient
    return len(s)

#100%
print(duplicate_count('Indivisibilities'))