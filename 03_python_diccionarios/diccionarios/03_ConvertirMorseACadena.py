#!/usr/bin/env python
if __name__ == '__main__':
    codigo = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--',
              ':': '---...', ';': '-.-.-.', '?': '..--..', '!': '-.-.--', '"': '.-..-.', "'": '.----.', '+': '.-.-.',
              '-': '-....-', '/': '-..-.', '=': '-...-', '_': '..--.-', '$': '...-..-', '@': '.--.-.', '&': '.-...',
              '(': '-.--.', ')': '-.--.-', ' ': ' '}
    palabraEnMorse = input("Escribe la palabra separando sus letras por espacios: ")
    palabrasMorse = palabraEnMorse.split(" ")
    palabra = ""
    for cod in palabrasMorse:
        letra = [key for key, valor in codigo.items() if valor == cod][0]
        palabra = palabra + letra
    print(palabra)
