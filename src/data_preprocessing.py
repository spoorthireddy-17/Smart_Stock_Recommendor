import pandas as pd
import numpy as np
import os

RAW_DATA_PATH = "data/raw/stock_data.csv"
PROCESSED_DATA_PATH = "data/processed/stock_features.csv"

os.makedirs("data/processed", exist_ok=True)

def preprocess_data():
    print("Loading dataset...")
    df = pd.read_csv(RAW_DATA_PATH)

    # Normalize column names
    df.columns = df.columns.str.lower().str.strip()

    # Rename symbol column if present
    if "symbol" in df.columns:
        df.rename(columns={"symbol": "stock"}, inplace=True)

    # Convert date column safely
    print("Converting date column...")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df.dropna(subset=["date"], inplace=True)

    # Sort data
    df = df.sort_values(["stock", "date"])

    # Calculate daily returns
    print("Calculating daily returns...")
    df["daily_return"] = df.groupby("stock")["close"].pct_change()

    # Aggregate features per stock
    features = df.groupby("stock").agg(
        avg_return=("daily_return", "mean"),
        volatility=("daily_return", "std"),
        avg_volume=("volume", "mean")
    )

    features.dropna(inplace=True)

    # ---------------- SAFE RISK SCORE ----------------
    EPSILON = 1e-4  # prevents division explosion

    features["risk_score"] = (
        features["volatility"] / (features["avg_return"].abs() + EPSILON)
    )

    # Log transform to reduce skewness
    features["risk_score"] = np.log1p(features["risk_score"])

    # Remove invalid values
    features.replace([np.inf, -np.inf], np.nan, inplace=True)
    features.dropna(inplace=True)

    # Save processed data
    features.to_csv(PROCESSED_DATA_PATH)

    print("✅ Preprocessing completed successfully!")
    print(f"Saved to: {PROCESSED_DATA_PATH}")
    print(f"Total stocks processed: {features.shape[0]}")

if __name__ == "__main__":
    preprocess_data()
