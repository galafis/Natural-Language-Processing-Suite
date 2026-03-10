"""
Stemmer Module
Simple rule-based stemming for English text.
"""

from typing import List


class PorterStemmerSimple:
    """Simplified Porter stemmer implementation."""

    SUFFIXES_STEP1 = [
        ("sses", "ss"), ("ies", "i"), ("ss", "ss"), ("s", ""),
    ]

    SUFFIXES_STEP2 = [
        ("ational", "ate"), ("tional", "tion"), ("enci", "ence"),
        ("anci", "ance"), ("izer", "ize"), ("abli", "able"),
        ("alli", "al"), ("entli", "ent"), ("eli", "e"),
        ("ousli", "ous"), ("ization", "ize"), ("ation", "ate"),
        ("ator", "ate"), ("alism", "al"), ("iveness", "ive"),
        ("fulness", "ful"), ("ousness", "ous"), ("aliti", "al"),
        ("iviti", "ive"), ("biliti", "ble"),
    ]

    SUFFIXES_STEP3 = [
        ("icate", "ic"), ("ative", ""), ("alize", "al"),
        ("iciti", "ic"), ("ical", "ic"), ("ful", ""), ("ness", ""),
    ]

    SUFFIXES_STEP4 = [
        "al", "ance", "ence", "er", "ic", "able", "ible",
        "ant", "ement", "ment", "ent", "ion", "ou", "ism",
        "ate", "iti", "ous", "ive", "ize",
    ]

    def stem(self, word: str) -> str:
        """Stem a single word."""
        word = word.lower().strip()
        if len(word) <= 2:
            return word

        # Step 1: Plural and past participle
        word = self._step1(word)
        # Step 2: Derivational suffixes
        word = self._step2(word)
        # Step 3: More derivational suffixes
        word = self._step3(word)
        # Step 4: Residual suffixes
        word = self._step4(word)
        # Step 5: Final cleanup
        word = self._step5(word)

        return word

    def stem_tokens(self, tokens: List[str]) -> List[str]:
        """Stem a list of tokens."""
        return [self.stem(t) for t in tokens]

    def _step1(self, word: str) -> str:
        for suffix, replacement in self.SUFFIXES_STEP1:
            if word.endswith(suffix):
                return word[: -len(suffix)] + replacement
        if word.endswith("eed"):
            stem = word[:-3]
            if self._measure(stem) > 0:
                return word[:-1]
        for suffix in ("ed", "ing"):
            if word.endswith(suffix):
                stem = word[: -len(suffix)]
                if self._has_vowel(stem):
                    word = stem
                    if word.endswith(("at", "bl", "iz")):
                        word += "e"
                    elif len(word) > 2 and word[-1] == word[-2] and word[-1] not in "lsz":
                        word = word[:-1]
                    break
        return word

    def _step2(self, word: str) -> str:
        for suffix, replacement in self.SUFFIXES_STEP2:
            if word.endswith(suffix):
                stem = word[: -len(suffix)]
                if self._measure(stem) > 0:
                    return stem + replacement
        return word

    def _step3(self, word: str) -> str:
        for suffix, replacement in self.SUFFIXES_STEP3:
            if word.endswith(suffix):
                stem = word[: -len(suffix)]
                if self._measure(stem) > 0:
                    return stem + replacement
        return word

    def _step4(self, word: str) -> str:
        for suffix in self.SUFFIXES_STEP4:
            if word.endswith(suffix):
                stem = word[: -len(suffix)]
                if self._measure(stem) > 1:
                    return stem
        return word

    def _step5(self, word: str) -> str:
        if word.endswith("e"):
            stem = word[:-1]
            if self._measure(stem) > 1:
                return stem
            if self._measure(stem) == 1 and not self._ends_cvc(stem):
                return stem
        if word.endswith("ll") and self._measure(word[:-1]) > 1:
            return word[:-1]
        return word

    def _measure(self, stem: str) -> int:
        """Calculate the measure (number of VC sequences) of a stem."""
        vowels = set("aeiou")
        m = 0
        prev_vowel = False
        for ch in stem:
            is_vowel = ch in vowels
            if prev_vowel and not is_vowel:
                m += 1
            prev_vowel = is_vowel
        return m

    def _has_vowel(self, stem: str) -> bool:
        return any(c in "aeiou" for c in stem)

    def _ends_cvc(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = set("aeiou")
        return (
            word[-1] not in vowels
            and word[-2] in vowels
            and word[-3] not in vowels
            and word[-1] not in "wxy"
        )
