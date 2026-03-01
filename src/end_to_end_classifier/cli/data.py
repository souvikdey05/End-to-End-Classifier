"""CLI commands for data operations."""

import logging
import typer
import pandas as pd

from end_to_end_classifier.config import DataConfig

app = typer.Typer(no_args_is_help=True)

@app.command()
def prepare_data() -> None:
    """Prepare data for training."""
    
    from end_to_end_classifier.data.preprocess import preprocess, inspect_columns
    
    data_config = DataConfig()
    data_f = pd.read_csv(data_config.raw_data_path)
    # inspect_columns(data_f)
    data_processed = preprocess(data_f)
    inspect_columns(data_processed)

    # print(data_processed.head())