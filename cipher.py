import string

# Definición de los símbolos soportados: letras, dígitos y puntuación
SYMBOLS = string.ascii_letters + string.digits + string.punctuation
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('\nWhat would you like to do today?')
        print('[E]ncrypt a message\n[D]ecrypt a message\n[B]rute force decryption\n[Q]uit')
        mode = input('Please select an option (E/D/B) or Q to quit: ').lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b', 'q']:
            return mode
        else:
            print('Invalid option, please choose either "E", "D", "B", or "Q".')

def getMessage():
    print('\nEnter the message:')
    return input()

def getKey():
    while True:
        try:
            key = int(input(f'Enter the key number (1-{MAX_KEY_SIZE}): '))
            if 1 <= key <= MAX_KEY_SIZE:
                return key
            else:
                print(f'Please enter a number between 1 and {MAX_KEY_SIZE}.')
        except ValueError:
            print('Invalid input. Please enter a numeric value.')

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            # Ajuste del índice para cifrar o descifrar
            symbolIndex += key
            
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            
            translated += SYMBOLS[symbolIndex]
        else:
            # Si el símbolo no está en SYMBOLS, se añade sin cambio.
            translated += symbol
    return translated

# Bucle principal para mantener el programa en ejecución
while True:
    mode = getMode()
    if mode == 'q':
        print('Exiting the program. Goodbye!')
        break
    message = getMessage()
    if mode != 'b':
        key = getKey()
        print('\nYour translated text is:')
        print(getTranslatedMessage(mode, message, key))
    else:
        print('\nAttempting brute force decryption:')
        for key in range(1, MAX_KEY_SIZE + 1):
            print(f'Key {key}: {getTranslatedMessage("decrypt", message, key)}')
