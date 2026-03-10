"""
Stop Words Module
Stop words removal for text preprocessing.
"""

from typing import List, Optional, Set


ENGLISH_STOP_WORDS = frozenset({
    "a", "about", "above", "after", "again", "against", "all", "am", "an",
    "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can",
    "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does",
    "doesn't", "doing", "don't", "down", "during", "each", "few", "for",
    "from", "further", "get", "got", "had", "hadn't", "has", "hasn't",
    "have", "haven't", "having", "he", "her", "here", "hers", "herself",
    "him", "himself", "his", "how", "i", "if", "in", "into", "is", "isn't",
    "it", "its", "itself", "just", "let", "me", "might", "more", "most",
    "mustn't", "my", "myself", "no", "nor", "not", "now", "of", "off",
    "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves",
    "out", "over", "own", "same", "shan't", "she", "should", "shouldn't",
    "so", "some", "such", "than", "that", "the", "their", "theirs", "them",
    "themselves", "then", "there", "these", "they", "this", "those",
    "through", "to", "too", "under", "until", "up", "very", "was", "wasn't",
    "we", "were", "weren't", "what", "when", "where", "which", "while",
    "who", "whom", "why", "will", "with", "won't", "would", "wouldn't",
    "you", "your", "yours", "yourself", "yourselves",
})

PORTUGUESE_STOP_WORDS = frozenset({
    "a", "ao", "aos", "aquela", "aquelas", "aquele", "aqueles", "aquilo",
    "as", "ate", "com", "como", "da", "das", "de", "dela", "delas", "dele",
    "deles", "depois", "do", "dos", "e", "ela", "elas", "ele", "eles", "em",
    "entre", "era", "essa", "essas", "esse", "esses", "esta", "estas",
    "este", "estes", "eu", "foi", "for", "foram", "ha", "isso", "isto",
    "ja", "lhe", "lhes", "lo", "mas", "me", "mesmo", "meu", "meus",
    "minha", "minhas", "muito", "na", "nas", "nao", "nas", "nem", "no",
    "nos", "nossa", "nossas", "nosso", "nossos", "num", "numa", "o", "os",
    "ou", "para", "pela", "pelas", "pelo", "pelos", "por", "qual", "quando",
    "que", "quem", "sao", "se", "sem", "sera", "seu", "seus", "so", "sua",
    "suas", "tambem", "te", "tem", "tendo", "tenho", "ter", "teu", "teus",
    "ti", "toda", "todas", "todo", "todos", "tu", "tua", "tuas", "tudo",
    "um", "uma", "umas", "uns", "voce", "voces", "vos",
})


class StopWordRemover:
    """Removes stop words from text."""

    def __init__(self, language: str = "en", custom_words: Optional[Set[str]] = None):
        self.language = language
        if language == "pt":
            self.stop_words = set(PORTUGUESE_STOP_WORDS)
        else:
            self.stop_words = set(ENGLISH_STOP_WORDS)
        if custom_words:
            self.stop_words.update(custom_words)

    def remove(self, tokens: List[str]) -> List[str]:
        """Remove stop words from a token list."""
        return [t for t in tokens if t.lower() not in self.stop_words]

    def is_stop_word(self, word: str) -> bool:
        """Check if a word is a stop word."""
        return word.lower() in self.stop_words

    def add_words(self, words: Set[str]):
        """Add custom stop words."""
        self.stop_words.update(w.lower() for w in words)

    def get_stop_words(self) -> Set[str]:
        """Return the current set of stop words."""
        return set(self.stop_words)
