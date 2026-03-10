"""
Tests for the Natural Language Processing Suite.
"""

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from tokenizer import Tokenizer
from stemmer import PorterStemmerSimple
from stopwords import StopWordRemover
from tfidf import TfidfVectorizer
from sentiment import LexiconSentimentAnalyzer
from naive_bayes import NaiveBayesClassifier
from word_frequency import WordFrequencyAnalyzer


class TestTokenizer:
    def setup_method(self):
        self.tokenizer = Tokenizer()

    def test_word_tokenize(self):
        tokens = self.tokenizer.word_tokenize("Hello world, this is a test.")
        assert "hello" in tokens
        assert "world" in tokens

    def test_sentence_tokenize(self):
        text = "First sentence. Second sentence. Third one."
        sentences = self.tokenizer.sentence_tokenize(text)
        assert len(sentences) == 3

    def test_ngrams(self):
        tokens = ["a", "b", "c", "d"]
        bigrams = self.tokenizer.ngrams(tokens, 2)
        assert len(bigrams) == 3
        assert bigrams[0] == ("a", "b")

    def test_empty_text(self):
        tokens = self.tokenizer.word_tokenize("")
        assert tokens == []

    def test_character_tokenize(self):
        chars = self.tokenizer.character_tokenize("a b c")
        assert chars == ["a", "b", "c"]


class TestStemmer:
    def setup_method(self):
        self.stemmer = PorterStemmerSimple()

    def test_stem_plural(self):
        assert self.stemmer.stem("cats") == "cat"
        assert self.stemmer.stem("ponies") == "poni"

    def test_stem_ing(self):
        result = self.stemmer.stem("running")
        assert result == "run"

    def test_stem_short_word(self):
        assert self.stemmer.stem("go") == "go"

    def test_stem_tokens(self):
        tokens = ["running", "cats", "played"]
        stemmed = self.stemmer.stem_tokens(tokens)
        assert len(stemmed) == 3


class TestStopWords:
    def setup_method(self):
        self.remover = StopWordRemover()

    def test_remove_stop_words(self):
        tokens = ["the", "cat", "is", "on", "the", "mat"]
        filtered = self.remover.remove(tokens)
        assert "the" not in filtered
        assert "cat" in filtered

    def test_is_stop_word(self):
        assert self.remover.is_stop_word("the")
        assert not self.remover.is_stop_word("python")

    def test_portuguese_stop_words(self):
        remover = StopWordRemover(language="pt")
        assert remover.is_stop_word("para")
        assert remover.is_stop_word("que")

    def test_custom_stop_words(self):
        remover = StopWordRemover(custom_words={"python", "java"})
        assert remover.is_stop_word("python")
        assert remover.is_stop_word("the")


class TestTfidfVectorizer:
    def setup_method(self):
        self.vectorizer = TfidfVectorizer()

    def test_fit_transform(self):
        docs = ["the cat sat on the mat", "the dog lay on the rug"]
        vectors = self.vectorizer.fit_transform(docs)
        assert len(vectors) == 2
        assert len(vectors[0]) == len(vectors[1])

    def test_vocabulary(self):
        docs = ["hello world", "hello python"]
        self.vectorizer.fit(docs)
        names = self.vectorizer.get_feature_names()
        assert "hello" in names
        assert "world" in names

    def test_transform_after_fit(self):
        docs = ["alpha beta", "gamma delta"]
        self.vectorizer.fit(docs)
        vectors = self.vectorizer.transform(["alpha gamma"])
        assert len(vectors) == 1

    def test_max_features(self):
        vectorizer = TfidfVectorizer(max_features=3)
        docs = ["one two three four five", "two three four"]
        vectors = vectorizer.fit_transform(docs)
        assert len(vectors[0]) == 3

    def test_not_fitted_error(self):
        with pytest.raises(RuntimeError):
            self.vectorizer.transform(["test"])


class TestSentimentAnalyzer:
    def setup_method(self):
        self.analyzer = LexiconSentimentAnalyzer()

    def test_positive_sentiment(self):
        result = self.analyzer.analyze("This product is excellent and amazing!")
        assert result["sentiment"] == "positive"
        assert result["compound"] > 0

    def test_negative_sentiment(self):
        result = self.analyzer.analyze("This is terrible and awful, the worst ever.")
        assert result["sentiment"] == "negative"
        assert result["compound"] < 0

    def test_neutral_sentiment(self):
        result = self.analyzer.analyze("The table is made of wood.")
        assert result["sentiment"] == "neutral"

    def test_negation(self):
        result = self.analyzer.analyze("This is not good at all.")
        assert result["compound"] < 0.05

    def test_batch_analysis(self):
        texts = ["I love this!", "I hate this.", "It is okay."]
        results = self.analyzer.analyze_batch(texts)
        assert len(results) == 3

    def test_empty_text(self):
        result = self.analyzer.analyze("")
        assert result["sentiment"] == "neutral"


class TestNaiveBayes:
    def setup_method(self):
        self.classifier = NaiveBayesClassifier()

    def test_fit_and_predict(self):
        texts = [
            "great product love it",
            "amazing quality excellent",
            "wonderful experience happy",
            "terrible quality hate it",
            "awful product disappointed",
            "worst experience angry",
        ]
        labels = ["positive", "positive", "positive",
                  "negative", "negative", "negative"]

        self.classifier.fit(texts, labels)
        pred = self.classifier.predict("great quality love")
        assert pred == "positive"

    def test_predict_proba(self):
        texts = ["good great", "bad terrible"]
        labels = ["pos", "neg"]
        self.classifier.fit(texts, labels)
        probs = self.classifier.predict_proba("good")
        assert "pos" in probs
        assert "neg" in probs
        assert abs(sum(probs.values()) - 1.0) < 1e-6

    def test_accuracy(self):
        texts = ["good", "bad", "good", "bad"]
        labels = ["pos", "neg", "pos", "neg"]
        self.classifier.fit(texts, labels)
        score = self.classifier.score(["good", "bad"], ["pos", "neg"])
        assert score == 1.0

    def test_not_fitted_error(self):
        with pytest.raises(RuntimeError):
            self.classifier.predict("test")

    def test_mismatched_lengths(self):
        with pytest.raises(ValueError):
            self.classifier.fit(["a", "b"], ["x"])


class TestWordFrequency:
    def setup_method(self):
        self.analyzer = WordFrequencyAnalyzer()

    def test_analyze(self):
        text = "the cat sat on the mat the cat"
        result = self.analyzer.analyze(text)
        assert result["total_tokens"] > 0
        assert result["unique_words"] > 0
        assert len(result["top_words"]) > 0

    def test_type_token_ratio(self):
        text = "hello hello hello world"
        result = self.analyzer.analyze(text)
        assert 0 < result["type_token_ratio"] < 1

    def test_compare_texts(self):
        t1 = "python machine learning data"
        t2 = "java machine learning code"
        result = self.analyzer.compare_texts(t1, t2)
        assert result["common_words"] > 0
        assert 0 < result["jaccard_similarity"] <= 1.0

    def test_with_stop_words(self):
        analyzer = WordFrequencyAnalyzer(stop_words={"the", "a", "an"})
        text = "the cat and a dog"
        result = analyzer.analyze(text)
        top_words = [w["word"] for w in result["top_words"]]
        assert "the" not in top_words


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
