MORSE_CODE_DICT = {'A': '.=', 'B': '=...',
                   'C': '=.=.', 'D': '=..', 'E': '.',
                   'F': '..=.', 'G': '==.', 'H': '....',
                   'I': '..', 'J': '.===', 'K': '=.=',
                   'L': '.=..', 'M': '==', 'N': '=.',
                   'O': '===', 'P': '.==.', 'Q': '==.=',
                   'R': '.=.', 'S': '...', 'T': '=',
                   'U': '..=', 'V': '...=', 'W': '.==',
                   'X': '=..=', 'Y': '=.==', 'Z': '==..',
                   '1': '.====', '2': '..===', '3': '...==',
                   '4': '....=', '5': '.....', '6': '=....',
                   '7': '==...', '8': '===..', '9': '====.',
                   '0': '=====', ', ': '==..==', '.': '.=.=.=',
                   '?': '..==..', '/': '=..=.', '=': '=....=',
                   '(': '=.==.', ')': '=.==.=',
                   '@': '=...=.'}


# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += '/ '

    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '
    decipher = ''
    citext = ''

    i = 0
    for letter in message:

        if letter != ' ' and letter != '/':

            i = 0

            citext += letter

        elif letter == '/':
            i += 1

            decipher += ' '
        elif i == 0:

            # accessing the keys using their values (reverse of encryption)
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
            citext = ''

    return decipher


def is_morsor(text: str):
    return text.count('.') + text.count('=') + text.count(' ') + text.count('/') == len(text)
