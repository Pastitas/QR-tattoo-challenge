# Caesar Cipher

translated = ''

i = 0
message = raw_input('Enter your message: ')

for symbol in message:

    if symbol.isalpha():

        num = ord(symbol)

        num += i



        if symbol.isupper():

            if num > ord('Z'):
                num -= 26

            elif num < ord('A'):

                num += 26

        elif symbol.islower():

            if num > ord('z'):

                num -= 26

            elif num < ord('a'):

                num += 26



        translated += chr(num)

    else:

        translated += symbol

    if (i >= 26):

        i = 0

    else:

        i = i + 1

print('Your translated text is: ' + translated)
