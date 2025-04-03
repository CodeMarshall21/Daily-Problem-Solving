def ConsequtiveCandV(str):
    i = 0
    j = 1
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    newStr = ""
    while(j < len(str)):
        if (str[i] in vowels and str[j] in consonants):
            newStr += 'V'
            i = j
        if (str[i] in consonants and str[j] in vowels):
            newStr += 'C'
            i = j
        j += 1
    if (str[i] in vowels):
            newStr += 'V'
            i = j
    elif (str[i] in consonants):
            newStr += 'C'
            i = j
    return newStr

str = "mississippi"
print(ConsequtiveCandV(str))
