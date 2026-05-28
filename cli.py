import typer
from typing import Optional
from datetime import datetime
from core.sync import aggregate_words, export_to_ical, DuolingoClient, MemriseClient

app = typer.Typer()


@app.command()
def sync(output: Optional[str] = typer.Option("words.ics", help="Output iCalendar file path")):
    """Fetch and aggregate word-of-the-day from multiple language-learning apps."""
    clients = [DuolingoClient(), MemriseClient()]
    words = aggregate_words(clients)
    export_to_ical(words, output or "words.ics")
    typer.echo(f"Exported {len(words)} words to {output}")


if __name__ == "__main__":
    app()