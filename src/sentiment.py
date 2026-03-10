"""
Sentiment Analysis Module
Lexicon-based sentiment analysis.
"""

import re
from typing import Dict, List, Tuple


class LexiconSentimentAnalyzer:
    """Lexicon-based sentiment analyzer inspired by VADER approach."""

    POSITIVE_WORDS = {
        "good": 1.5, "great": 2.0, "excellent": 2.5, "amazing": 2.5,
        "wonderful": 2.5, "fantastic": 2.5, "outstanding": 2.5,
        "awesome": 2.0, "love": 2.0, "best": 2.0, "happy": 1.5,
        "beautiful": 1.5, "nice": 1.0, "perfect": 2.5, "brilliant": 2.0,
        "superb": 2.5, "impressive": 2.0, "delightful": 2.0,
        "enjoy": 1.5, "pleased": 1.5, "satisfied": 1.5, "positive": 1.0,
        "recommend": 1.5, "like": 1.0, "helpful": 1.5, "easy": 1.0,
        "fast": 1.0, "reliable": 1.5, "quality": 1.5, "thank": 1.0,
        "well": 1.0, "better": 1.5, "improved": 1.5, "effective": 1.5,
    }

    NEGATIVE_WORDS = {
        "bad": -1.5, "terrible": -2.5, "horrible": -2.5, "awful": -2.5,
        "worst": -2.5, "hate": -2.5, "poor": -1.5, "ugly": -1.5,
        "boring": -1.5, "annoying": -1.5, "disappointing": -2.0,
        "useless": -2.0, "broken": -1.5, "slow": -1.0, "difficult": -1.0,
        "expensive": -1.0, "problem": -1.5, "error": -1.5, "fail": -2.0,
        "failure": -2.0, "wrong": -1.5, "waste": -2.0, "never": -1.0,
        "worst": -2.5, "unhappy": -1.5, "angry": -2.0, "frustrated": -2.0,
        "confusing": -1.5, "complicated": -1.0, "crash": -2.0,
        "bug": -1.5, "issue": -1.0, "lacks": -1.0, "missing": -1.0,
    }

    NEGATION_WORDS = {"not", "no", "never", "neither", "nor", "none", "nobody",
                      "nothing", "nowhere", "hardly", "barely", "scarcely",
                      "don't", "doesn't", "didn't", "won't", "wouldn't",
                      "couldn't", "shouldn't", "isn't", "aren't", "wasn't"}

    INTENSIFIERS = {"very": 1.3, "really": 1.3, "extremely": 1.5,
                    "absolutely": 1.5, "totally": 1.4, "incredibly": 1.4,
                    "highly": 1.3, "so": 1.2, "quite": 1.1, "rather": 1.1}

    def analyze(self, text: str) -> Dict:
        """
        Analyze sentiment of text.

        Returns:
            Dict with sentiment label, compound score, and pos/neg/neu scores.
        """
        tokens = self._tokenize(text)
        if not tokens:
            return {"sentiment": "neutral", "compound": 0.0,
                    "positive": 0.0, "negative": 0.0, "neutral": 1.0}

        scores = []
        i = 0
        while i < len(tokens):
            token = tokens[i]
            score = 0.0

            # Check positive/negative lexicon
            if token in self.POSITIVE_WORDS:
                score = self.POSITIVE_WORDS[token]
            elif token in self.NEGATIVE_WORDS:
                score = self.NEGATIVE_WORDS[token]

            if score != 0.0:
                # Check for preceding negation
                if i > 0 and tokens[i - 1] in self.NEGATION_WORDS:
                    score *= -0.75
                # Check for intensifier
                if i > 0 and tokens[i - 1] in self.INTENSIFIERS:
                    score *= self.INTENSIFIERS[tokens[i - 1]]

            scores.append(score)
            i += 1

        # Compute compound score
        pos_sum = sum(s for s in scores if s > 0)
        neg_sum = sum(s for s in scores if s < 0)
        total = pos_sum + abs(neg_sum)

        if total == 0:
            compound = 0.0
        else:
            compound = (pos_sum + neg_sum) / (total + 5.0)  # Normalize

        # Check for exclamation marks (boost intensity)
        if "!" in text:
            compound *= 1.1

        # Clamp
        compound = max(-1.0, min(1.0, compound))

        # Compute proportions
        n = len(scores) if scores else 1
        pos_prop = sum(1 for s in scores if s > 0) / n
        neg_prop = sum(1 for s in scores if s < 0) / n
        neu_prop = 1.0 - pos_prop - neg_prop

        # Determine label
        if compound >= 0.05:
            label = "positive"
        elif compound <= -0.05:
            label = "negative"
        else:
            label = "neutral"

        return {
            "sentiment": label,
            "compound": round(compound, 4),
            "positive": round(pos_prop, 4),
            "negative": round(neg_prop, 4),
            "neutral": round(neu_prop, 4),
        }

    def analyze_batch(self, texts: List[str]) -> List[Dict]:
        """Analyze sentiment for a list of texts."""
        return [self.analyze(t) for t in texts]

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"[a-z']+", text.lower())
