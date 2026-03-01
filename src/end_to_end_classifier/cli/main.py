"""CLI entry point for end_to_end_classifier."""

import typer

from end_to_end_classifier.cli import data

app = typer.Typer(no_args_is_help=True)

app.add_typer(data.app, name="data")

if __name__ == "__main__":
    app()
