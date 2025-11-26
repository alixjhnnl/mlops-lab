from pathlib import Path
from typing import Union
import pandas as pd
import numpy as np
import os
import sys
import argparse
import logging
from sklearn.model_selection import train_test_split

# -------------------------------------------------------------------
#  Global Configuration
# -------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[4]
DATASTORE_DIR = PROJECT_ROOT / "datastores" 

OUTPUT_DIR = DATASTORE_DIR / "split_data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LOG_DIR = DATASTORE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------------
#  Logging Configuration
# -------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(f"{LOG_DIR}/data_split.log", mode="a"),
    ],
)
logger = logging.getLogger("data_split")

logger.info(f"PROJECT_ROOT: {PROJECT_ROOT}")

# -------------------------------------------------------------------
#  Functions
# -------------------------------------------------------------------
def load_data(input_data_path: Union[str, Path]) -> pd.DataFrame:
    """
    Loads a CSV file into a Pandas DataFrame.

    Args:
        input_data_path (Union[str, Path]): Path to the input CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    logger.info("Loading clean dataset...")
    try:
        input_path = Path(input_data_path)
        logger.info(f"Loading clean data from: {input_path}")
        df = pd.read_csv(input_path)
        logger.info(f"Successfully loaded dataset with shape {df.shape}")
        return df
    
    except FileNotFoundError:
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    except Exception as e:
        logger.error(f"Error loading data: {e}")
        sys.exit(1)


def split_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Spliting data")

    df_train, df_test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True, stratify=df[' salary'])

    return df_train, df_test


def save_data(df_train: pd.DataFrame, df_test: pd.DataFrame) -> Path:

    logger.info('Saving multiple artifacts files')
    file_paths = {"train_data.csv": df_train,
                  "test_data.csv": df_test}

    for filename, df in file_paths.items():
        df.to_csv(OUTPUT_DIR / filename, index=False)
        logger.info(f"save split data : {filename} : into datastores")

# -------------------------------------------------------------------
#  CLI Interface
# -------------------------------------------------------------------
def parse_arguments() -> argparse.Namespace:
    """
    Parses CLI arguments for the preprocessing step.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Split data - separate clean dataset for MLOps pipeline"
    )

    parser.add_argument(
        "--input_data_path",
        type=str,
        required=True,
        help="Path to the clean input CSV file.",
    )



    return parser.parse_args()


# -------------------------------------------------------------------
#  Main Entry Point
# -------------------------------------------------------------------
def main() -> None:
    """
    Main function for CLI execution.
    Loads, cleans, and saves data in one reproducible pipeline step.
    """
    args = parse_arguments()

    df_clean=load_data(args.input_data_path) 
    df_train, df_test =split_data(df_clean) 
    save_data(df_train, df_test) 


if __name__ == "__main__":
    main()
 