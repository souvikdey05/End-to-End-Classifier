"""CLI commands for data operations."""

import logging

import typer

app = typer.Typer(no_args_is_help=True)

@app.command()
def prepare_data() -> None:
    """Prepare data for training."""
    pass