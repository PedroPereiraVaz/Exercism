import secrets
import string

class Cipher:
    def __init__(self, key=None):
        if not key:
            key = ''.join([secrets.choice(string.ascii_lowercase) for _ in range(100)])

        self.key = key


    def encode(self, text):

        encode_text = ""
        
        for i in range(len(text)):
            encode_text += self.calculate_letter(text[i], self.key[i % len(self.key)])

        return encode_text

    def decode(self, text):

        decode_text = ""
        
        for i in range(len(text)):
            decode_text += self.calculate_letter(text[i], self.key[i % len(self.key)], -1)

        return decode_text
    def calculate_letter(self, letter, disp, operation=1):
        ascii_a = 97
        letter = ord(letter) - ascii_a
        disp = ord(disp) - ascii_a
        return  chr((letter + disp * operation) % 26 + ascii_a)
