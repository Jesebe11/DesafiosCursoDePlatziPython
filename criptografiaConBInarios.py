from textwrap import wrap

KEYS = {
'a': '00000001',
'b': '00000010',
'c': '00000011',
'd': '00000100',
'e': '00000101',
'f': '00000110',
'g': '00000111',
'h': '00001000',
'i': '00001001',
'j': '00010000',
'k': '00010001',
'l': '00010010',
'm': '00010011',
'n': '00010100',
'o': '00010101',
'p': '00010110',
'q': '00010111',
'r': '00011000',
's': '00011001',
't': '00100000',
'u': '00100001',
'v': '00100010',
'w': '00100011',
'x': '00100100',
'y': '00100101',
'z': '00100110',
'A': '00100111',
'B': '00101000',
'C': '00101001',
'D': '00110000',
'E': '00110001',
'F': '00110010',
'G': '00110011',
'H': '00110100',
'I': '00110101',
'J': '00110110',
'K': '00110111',
'L': '00111000',
'M': '00111001',
'N': '01000000',
'O': '01000001',
'P': '01000010',
'Q': '01000011',
'R': '01000100',
'S': '01000101',
'T': '01000110',
'U': '01000111',
'V': '01001000',
'W': '01001001',
'X': '01010000',
'Y': '01010001',
'Z': '01010010',
'0': '01010011',
'1': '01010100',
'2': '01010101',
'3': '01010110',
'4': '01010111',
'5': '01011000',
'6': '01011001',
'7': '01100000',
'8': '01100001',
'9': '01100010',
'.': '01100011',
',': '01100100',
'?': '01100101',
'!': '01100110',
}

def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return' '.join(cypher_message)


def decipher(message):
    #words = message.split(' ')
    words = wrap(message, 8)
    
    decipher_message = []

    decipher_word = ''

    for letter in words:
        for key, value in KEYS.items():

            if value == letter:
                decipher_word += key

    decipher_message.append(decipher_word)

    return' '.join(decipher_message)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía con números binarios. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('salir')
            exit()
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()