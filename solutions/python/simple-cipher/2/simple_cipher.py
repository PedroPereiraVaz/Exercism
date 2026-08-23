"""Module cipher"""
import secrets
import string
from typing import Optional

class Cipher:
    """Class for Cipher"""
    def __init__(self, key: Optional[str] = None) -> None:
        if not key:
            key = ''.join([secrets.choice(string.ascii_lowercase) for _ in range(100)])

        self.key = key


    def encode(self, text:str) -> str:
        """Encode Cipher"""
        return ''.join(
            self._calculate_letter(char, self.key[i % len(self.key)], operation=1)
            for i, char in enumerate(text)
        )

    def decode(self, text):
        """Decode Cipher"""
        return ''.join(
            self._calculate_letter(char, self.key[i % len(self.key)], operation=-1)
            for i, char in enumerate(text)
        )

    def _calculate_letter(self, char: str, key_char: str, operation: int) -> str:
        """Calculate letter"""
        base = ord('a')

        char_val = ord(char) - base
        key_val = ord(key_char) - base

        return chr((char_val + (key_val * operation)) % 26 + base)
