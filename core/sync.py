from typing import List, Dict, Optional
from datetime import datetime
import requests
from icalendar import Calendar, Event

class LanguageAppClient:
    """Base class for language app clients."""

    def fetch_word_of_the_day(self) -> Optional[Dict[str, str]]:
        """Fetch word-of-the-day from the app."""
        raise NotImplementedError


class DuolingoClient(LanguageAppClient):
    """Mock client for Duolingo."""

    def fetch_word_of_the_day(self) -> Optional[Dict[str, str]]:
        """Fetch word-of-the-day from Duolingo."""
        # In a real implementation, this would call the Duolingo API
        return {
            "word": "bonjour",
            "language": "French",
            "definition": "hello",
            "source": "Duolingo",
            "date": datetime.now().strftime("%Y-%m-%d"),
        }


class MemriseClient(LanguageAppClient):
    """Mock client for Memrise."""

    def fetch_word_of_the_day(self) -> Optional[Dict[str, str]]:
        """Fetch word-of-the-day from Memrise."""
        return {
            "word": "hola",
            "language": "Spanish",
            "definition": "hello",
            "source": "Memrise",
            "date": datetime.now().strftime("%Y-%m-%d"),
        }


def aggregate_words(clients: List[LanguageAppClient]) -> List[Dict[str, str]]:
    """Aggregate word-of-the-day from multiple clients."""
    words = []
    for client in clients:
        word = client.fetch_word_of_the_day()
        if word:
            words.append(word)
    return words


def export_to_ical(words: List[Dict[str, str]], output_path: str) -> None:
    """Export words to an iCalendar file."""
    cal = Calendar()
    for word in words:
        event = Event()
        event.add("summary", f"{word['word']} ({word['language']})")
        event.add("description", word["definition"])
        event.add("dtstart", datetime.strptime(word["date"], "%Y-%m-%d"))
        event.add("dtend", datetime.strptime(word["date"], "%Y-%m-%d"))
        cal.add_component(event)
    with open(output_path, "wb") as f:
        f.write(cal.to_ical())


if __name__ == "__main__":
    clients = [DuolingoClient(), MemriseClient()]
    words = aggregate_words(clients)
    export_to_ical(words, "words.ics")
    print(f"Exported {len(words)} words to words.ics")