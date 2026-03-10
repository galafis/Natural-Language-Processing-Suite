"""
Naive Bayes Classifier Module
Text classification using Multinomial Naive Bayes.
"""

import math
import re
from collections import Counter, defaultdict
from typing import Dict, List, Optional, Tuple


class NaiveBayesClassifier:
    """Multinomial Naive Bayes for text classification."""

    def __init__(self, alpha: float = 1.0):
        """
        Args:
            alpha: Laplace smoothing parameter.
        """
        self.alpha = alpha
        self.class_log_priors_ = {}
        self.feature_log_probs_ = {}
        self.vocabulary_ = set()
        self.classes_ = []
        self._fitted = False

    def fit(self, texts: List[str], labels: List[str]) -> "NaiveBayesClassifier":
        """Train the classifier."""
        if len(texts) != len(labels):
            raise ValueError("texts and labels must have the same length")

        class_counts = Counter(labels)
        self.classes_ = sorted(class_counts.keys())
        total_docs = len(texts)

        # Compute log priors
        self.class_log_priors_ = {
            cls: math.log(count / total_docs)
            for cls, count in class_counts.items()
        }

        # Tokenize and build vocabulary
        tokenized = [self._tokenize(t) for t in texts]
        self.vocabulary_ = set()
        for tokens in tokenized:
            self.vocabulary_.update(tokens)

        vocab_size = len(self.vocabulary_)

        # Compute feature log probabilities per class
        class_word_counts = defaultdict(Counter)
        class_total_words = defaultdict(int)

        for tokens, label in zip(tokenized, labels):
            for token in tokens:
                class_word_counts[label][token] += 1
                class_total_words[label] += 1

        self.feature_log_probs_ = {}
        for cls in self.classes_:
            total = class_total_words[cls]
            self.feature_log_probs_[cls] = {}
            for word in self.vocabulary_:
                count = class_word_counts[cls][word]
                self.feature_log_probs_[cls][word] = math.log(
                    (count + self.alpha) / (total + self.alpha * vocab_size)
                )

        self._fitted = True
        return self

    def predict(self, text: str) -> str:
        """Predict the class of a single text."""
        probs = self.predict_proba(text)
        return max(probs, key=probs.get)

    def predict_proba(self, text: str) -> Dict[str, float]:
        """Predict class probabilities."""
        if not self._fitted:
            raise RuntimeError("Classifier must be fitted first.")

        tokens = self._tokenize(text)
        log_probs = {}

        for cls in self.classes_:
            log_prob = self.class_log_priors_[cls]
            for token in tokens:
                if token in self.feature_log_probs_[cls]:
                    log_prob += self.feature_log_probs_[cls][token]
            log_probs[cls] = log_prob

        # Convert to probabilities using log-sum-exp
        max_log = max(log_probs.values())
        exp_sum = sum(math.exp(lp - max_log) for lp in log_probs.values())

        probs = {}
        for cls, lp in log_probs.items():
            probs[cls] = math.exp(lp - max_log) / exp_sum

        return probs

    def predict_batch(self, texts: List[str]) -> List[str]:
        """Predict classes for multiple texts."""
        return [self.predict(t) for t in texts]

    def score(self, texts: List[str], labels: List[str]) -> float:
        """Compute accuracy on labeled data."""
        predictions = self.predict_batch(texts)
        correct = sum(1 for p, l in zip(predictions, labels) if p == l)
        return correct / len(labels) if labels else 0.0

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"[a-z]+", text.lower())
