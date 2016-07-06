#definition
def anti_vowel(text):
    #value to hold new string
    b = ''
    #for loop to chceck single letter
    for a in range(len(text)):
        #if the letter is in that string, do nothing; continue
        if (text[a] in "aeiouAEIOU"):
            continue
        #add to the string
        else:
            b += text[a]
    return b

print anti_vowel("Asado qwe Oirjan qw eanf tuc")
