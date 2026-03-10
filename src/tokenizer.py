"""
Tokenizer Module
Text tokenization with multiple strategies.
"""

import re
from typing import List, Optional


class Tokenizer:
    """Tokenizes text into words, sentences, or n-grams."""

    def __init__(self, lowercase: bool = True):
        self.lowercase = lowercase

    def word_tokenize(self, text: str) -> List[str]:
        """Split text into word tokens."""
        if self.lowercase:
            text = text.lower()
        tokens = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?\b|\b\d+(?:\.\d+)?\b", text)
        return tokens

    def sentence_tokenize(self, text: str) -> List[str]:
        """Split text into sentences."""
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text.strip())
        return [s.strip() for s in sentences if s.strip()]

    def ngrams(self, tokens: List[str], n: int) -> List[tuple]:
        """Generate n-grams from token list."""
        if n < 1 or n > len(tokens):
            return []
        return [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]

    def character_tokenize(self, text: str) -> List[str]:
        """Split text into individual characters (excluding whitespace)."""
        return [c for c in text if not c.isspace()]
