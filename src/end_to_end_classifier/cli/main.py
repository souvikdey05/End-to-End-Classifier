"""CLI entry point for end_to_end_classifier."""

import logging
import typer

from end_to_end_classifier.cli import data

app = typer.Typer(no_args_is_help=True)

app.add_typer(data.app, name="data")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    
    app()
