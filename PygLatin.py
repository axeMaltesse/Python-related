#Create a variable to add letters to the string
pyg = 'ay'
#Enter your word
original = raw_input('Enter a word:')
#simple function to hash the message
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'
