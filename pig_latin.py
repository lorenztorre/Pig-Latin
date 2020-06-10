word = input('What is your word? \n\n').lower()

def pig_latin(word):
    if word[0] in 'a,e,i,o,u':
        print('\n' + word + 'ay')
    else: 
        print('\n' +word[1:] + word[0] + 'ay')

pig_latin(word)
