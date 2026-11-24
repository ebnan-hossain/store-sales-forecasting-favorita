
import pandas as pd
from pathlib import Path

#approach: Define the dataset directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

#approach: Load all seven CSV files
holidays = pd.read_csv(DATA_DIR / "holidays_events.csv")
oil = pd.read_csv(DATA_DIR / "oil.csv")
sample_submission = pd.read_csv(DATA_DIR / "sample_submission.csv")
stores = pd.read_csv(DATA_DIR / "stores.csv")
test = pd.read_csv(DATA_DIR / "test.csv")
train = pd.read_csv(DATA_DIR / "train.csv")
transactions = pd.read_csv(DATA_DIR / "transactions.csv")

#approach: Store the DataFrames in a dictionary
datasets = {
    "holidays": holidays,
    "oil": oil,
    "sample_submission": sample_submission,
    "stores": stores,
    "test": test,
    "train": train,
    "transactions": transactions
}

#approach: Verify successful loading
for name, df in datasets.items():
    print(f"{name}: Loaded successfully | Shape: {df.shape}")


#approach: Inspect column names and data types
for name, df in datasets.items():

    print("\n" + "=" * 60)
    print(f"DATASET: {name.upper()}")
    print("=" * 60)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)


#approach: Analyze missing values in all datasets
for name, df in datasets.items():

    print("\n" + "=" * 60)
    print(f"MISSING VALUE ANALYSIS: {name.upper()}")
    print("=" * 60)

    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / len(df)) * 100

    missing_summary = pd.DataFrame({
        "Missing Values": missing_count,
        "Missing Percentage": missing_percentage
    })

    print(missing_summary)
