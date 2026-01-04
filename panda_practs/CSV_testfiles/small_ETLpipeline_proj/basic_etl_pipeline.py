import pandas as pd 
import time
import functools

# Build a simple ETL (Extract, Transform, Load) pipeline for CSV-based operational data, using:
# - Decorators to add logging, timing, and error handling.
# - pandas for data cleaning and transformation.
# - Modular, annotated code for auditability.

# 1.- Decorators for auditability
def log_step(func):
    """Log function execution for auditability."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished: {func.__name__}")
        return result 
    return wrapper

def time_step(func):
    """Measure execution time of each step."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[TIME] {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

# 2.- ETL Pipeline functions
@log_step
@time_step
def extract(path: str) -> pd.DataFrame:
    """Extract data from CSV."""
    return pd.read_csv(path)

@log_step
@time_step
def transform(df: pd.DataFrame) -> pd.DataFrame:
        """Clean and transform data."""
        # fill missing amounts (N/A) with 0
        df['amount'] = df['amount'].fillna(0)

        # convert date to datetime
        df['date'] = pd.to_datetime(df['date'])

        # aggregate sales per customer
        summary = df.groupby('customer')['amount'].sum().reset_index()
        return summary

@log_step
@time_step
def load(df: pd.DataFrame, path: str):
    """Load transformed data to CSV."""
    df.to_csv(path, index=False)
    print(f"[LOAD] Data written to {path}")

# 3.- Pipeline orchestration
def run_pipeline():
     raw = extract("sales.csv")
     transformed = transform(raw)
     load(transformed, "sales_summary.csv")

run_pipeline()