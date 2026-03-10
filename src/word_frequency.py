"""
Word Frequency Analysis Module
Analyze word frequency distributions in text.
"""

import re
from collections import Counter
from typing import Dict, List, Optional, Set, Tuple


class WordFrequencyAnalyzer:
    """Analyzes word frequency distributions."""

    def __init__(self, stop_words: Optional[Set[str]] = None):
        self.stop_words = stop_words or set()

    def analyze(self, text: str, top_k: int = 20) -> Dict:
        """
        Perform complete word frequency analysis.

        Returns:
            Dict with frequency distribution, statistics, and top words.
        """
        tokens = self._tokenize(text)
        filtered = [t for t in tokens if t not in self.stop_words]
        freq = Counter(filtered)

        total = len(filtered)
        unique = len(freq)

        top_words = [
            {"word": word, "count": count, "frequency": round(count / total, 6) if total else 0}
            for word, count in freq.most_common(top_k)
        ]

        # Hapax legomena (words appearing only once)
        hapax = [word for word, count in freq.items() if count == 1]

        return {
            "total_tokens": len(tokens),
            "filtered_tokens": total,
            "unique_words": unique,
            "type_token_ratio": round(unique / total, 4) if total else 0,
            "hapax_legomena": len(hapax),
            "top_words": top_words,
        }

    def get_frequency_distribution(self, text: str) -> Counter:
        """Get raw frequency distribution."""
        tokens = self._tokenize(text)
        filtered = [t for t in tokens if t not in self.stop_words]
        return Counter(filtered)

    def compare_texts(self, text1: str, text2: str, top_k: int = 10) -> Dict:
        """Compare word frequencies between two texts."""
        freq1 = self.get_frequency_distribution(text1)
        freq2 = self.get_frequency_distribution(text2)

        common = set(freq1.keys()) & set(freq2.keys())
        only_in_1 = set(freq1.keys()) - set(freq2.keys())
        only_in_2 = set(freq2.keys()) - set(freq1.keys())

        return {
            "common_words": len(common),
            "unique_to_text1": len(only_in_1),
            "unique_to_text2": len(only_in_2),
            "jaccard_similarity": round(
                len(common) / len(common | only_in_1 | only_in_2), 4
            ) if (common or only_in_1 or only_in_2) else 0,
            "top_common": sorted(
                [{"word": w, "freq1": freq1[w], "freq2": freq2[w]} for w in common],
                key=lambda x: x["freq1"] + x["freq2"],
                reverse=True,
            )[:top_k],
        }

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"[a-z]+", text.lower())
