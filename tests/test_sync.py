import pytest
from core.sync import aggregate_words, DuolingoClient, MemriseClient


def test_aggregate_words():
    """Test word aggregation from multiple clients."""
    clients = [DuolingoClient(), MemriseClient()]
    words = aggregate_words(clients)
    assert len(words) == 2
    assert words[0]["word"] == "bonjour"
    assert words[1]["word"] == "hola"


def test_duolingo_client():
    """Test Duolingo client."""
    client = DuolingoClient()
    word = client.fetch_word_of_the_day()
    assert word["word"] == "bonjour"
    assert word["language"] == "French"


def test_memrise_client():
    """Test Memrise client."""
    client = MemriseClient()
    word = client.fetch_word_of_the_day()
    assert word["word"] == "hola"
    assert word["language"] == "Spanish"