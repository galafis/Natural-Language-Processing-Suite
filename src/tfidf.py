"""
TF-IDF Vectorizer Module
Term Frequency-Inverse Document Frequency implementation.
"""

import math
import re
from collections import Counter
from typing import Dict, List, Optional, Tuple


class TfidfVectorizer:
    """TF-IDF vectorizer for document representation."""

    def __init__(self, max_features: Optional[int] = None, min_df: int = 1):
        self.max_features = max_features
        self.min_df = min_df
        self.vocabulary_ = {}
        self.idf_ = {}
        self._fitted = False

    def fit(self, documents: List[str]) -> "TfidfVectorizer":
        """Fit the vectorizer on a corpus."""
        tokenized = [self._tokenize(doc) for doc in documents]
        n_docs = len(documents)

        # Compute document frequency
        df = Counter()
        for tokens in tokenized:
            for token in set(tokens):
                df[token] += 1

        # Filter by min_df
        filtered = {t: f for t, f in df.items() if f >= self.min_df}

        # Sort by frequency and limit features
        sorted_terms = sorted(filtered.items(), key=lambda x: x[1], reverse=True)
        if self.max_features:
            sorted_terms = sorted_terms[:self.max_features]

        self.vocabulary_ = {term: idx for idx, (term, _) in enumerate(sorted_terms)}
        self.idf_ = {
            term: math.log((n_docs + 1) / (freq + 1)) + 1
            for term, freq in sorted_terms
        }
        self._fitted = True
        return self

    def transform(self, documents: List[str]) -> List[List[float]]:
        """Transform documents into TF-IDF vectors."""
        if not self._fitted:
            raise RuntimeError("Vectorizer must be fitted before transform.")

        vectors = []
        vocab_size = len(self.vocabulary_)

        for doc in documents:
            tokens = self._tokenize(doc)
            tf = Counter(tokens)
            total = len(tokens) if tokens else 1

            vector = [0.0] * vocab_size
            for term, idx in self.vocabulary_.items():
                if term in tf:
                    tf_val = tf[term] / total
                    vector[idx] = tf_val * self.idf_.get(term, 0)
            vectors.append(vector)

        return vectors

    def fit_transform(self, documents: List[str]) -> List[List[float]]:
        """Fit and transform in one step."""
        self.fit(documents)
        return self.transform(documents)

    def get_feature_names(self) -> List[str]:
        """Return feature names (vocabulary terms)."""
        items = sorted(self.vocabulary_.items(), key=lambda x: x[1])
        return [term for term, _ in items]

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"[a-z]+", text.lower())
