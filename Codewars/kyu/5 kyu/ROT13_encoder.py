#A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

def rot13(message):
    encoder = str.maketrans({'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r',
               'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
               'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
               'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
               'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
               'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
               'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
               'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B',
               'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
               'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M',})
    cipher = message.translate(encoder)
    return cipher

print(rot13('Aa Bb Cc 123!@'))
#100%