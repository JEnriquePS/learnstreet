#Morse Code project
to_morse = {
        'a': '.-',         'b': '-...',      'c': '-.-.',
        'd': '-..',        'e': '.',         'f': '..-.',
        'g': '--.',        'h': '....',      'i': '..',
        'j': '.---',       'k': '-.-',       'l': '.-..',
        'm': '--',         'n': '-.',        'o': '---',
        'p': '.--.',       'q': '--.-',      'r': '.-.',
        's': '...',        't': '-',         'u': '..-',
        'v': '...-',       'w': '.--',       'x': '-..-',
        'y': '-.--',       'z': '--..',
        '0': '-----',      '1': '.----',     '2': '..---',
        '3': '...--',      '4': '....-',     '5': '.....',
        '6': '-....',      '7': '--...',     '8': '---..',
        '9': '----.',
        ',': '--..--',     '.': '.-.-.-',    '?': '..--..',
        ';': '-.-.-.',     ':': '---...',    "'": '.----.',
        '-': '-....-',     '/': '-..-.',     '_': '..--.-',
        '(': '-.--.',      ')': '-.--.-'
}
from_morse = dict((b,a) for a,b in to_morse.items()) 

def morse(string_word):
    '''Convert a single word, string_word, to Morse code using to_morse above.'''
    '''Note that Morse code is not case-sensitive, so you will want to convert upper case letters to lower case.'''
    newchar = ' '
    caracter = string_word.lower()
    for caracteres in caracter:
        if caracteres in caracter:
            newchar += to_morse[caracteres] +  ' '
        else:
            print('no hay valor para %r' %caracteres)
    return newchar
        
def str_morse(sentence):
    '''Translate multiple words in a sentence encoded in Morse code, using your morse() function above.'''
    '''REPLACE THIS CODE WITH YOUR "morse" METHOD.'''
    string = sentence.split(' ')
    res_morse = ''
    for s in string:
        res_morse = res_morse+''+morse(s)
    res_morse = res_morse.strip()
    return res_morse
    
def string(morse_word):
    '''Convert a single Morse code word, morse_word, into normal text using from_morse above.'''
    '''REPLACE THIS CODE WITH YOUR "morse" METHOD.'''
    string = ''
    for word in morse_word.split('   '):
        for char in morse_word.split():
            if char in from_morse:
                string += from_morse[char]
            else:
                print('Value for %r not found as morse.' % char)
    return string
    
def morse_str(morse_sentence):
    '''Convert a sentence in Morse code, splitting out the words and passing them to your new string() function above.'''
    '''REPLACE THIS CODE WITH YOUR "morse" METHOD.'''  
    morse_sentence=morse_sentence.split('  ')
    res_string=''
    for s in morse_sentence:
        res_string=res_string+' '+string(s)
    res_string=res_string.strip()
    return res_string
    