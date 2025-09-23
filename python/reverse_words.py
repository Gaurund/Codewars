'''
Complete the function that accepts a string parameter, 
and reverses each word in the string. 
All spaces in the string should be retained.
'''


test_string = '  stressed desserts   '

def reverse_words(text):
    words = text.split()
    counter = 0
    index = 0
    result = ''
    while index < len(text):
        if(text[index]==' '):
            result += ' '
            index += 1
        else:
            result += words[counter][::-1]
            index += len(words[counter])
            counter += 1

    return result

def reverse_words_not_mine(str):
    r =' '.join(s[::-1] for s in str.split(' '))
    return r

print(reverse_words_not_mine(test_string))
    
