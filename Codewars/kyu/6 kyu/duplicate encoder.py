def duplicate_encoder(string):
    encoded = ''
    if string != None:
        formatted_string = string.lower()
        for s in formatted_string:
            if formatted_string.count(s) > 1:
                encoded += ')'
            else:
                encoded += '('
    print(encoded)

#100%
duplicate_encoder(None)
duplicate_encoder('recede')
duplicate_encoder('Success')
duplicate_encoder('(( @')

