"""Module cipher"""
import secrets
import string
from typing import Optional

class Cipher:
    """Class for Cipher"""
    def __init__(self, key: Optional[str] = None) -> None:
        if not key:
            key = ''.join(secrets.choice(string.ascii_lowercase) for iteration in range(100))

        self.key = key

    def encode(self, text: str) -> str:
        """Encode Cipher"""
        return ''.join(
            self._calculate_letter(char, self.key[index % len(self.key)], operation=1)
            for index, char in enumerate(text) # Linter fix: Cambiamos 'i' por 'index'
        )

    def decode(self, text: str) -> str:
        """Decode Cipher"""
        return ''.join(
            self._calculate_letter(char, self.key[index % len(self.key)], operation=-1)
            for index, char in enumerate(text) # Linter fix: Cambiamos 'i' por 'index'
        )

    @staticmethod
    def _calculate_letter(char: str, key_char: str, operation: int) -> str:
        """Calculate letter"""
        base = ord('a')

        char_val = ord(char) - base
        key_val = ord(key_char) - base

        return chr((char_val + (key_val * operation)) % 26 + base)