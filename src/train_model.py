import pandas as pd
import os

FEATURES_PATH = "data/processed/stock_features.csv"

def assign_risk_levels():
    print("Loading features...")
    df = pd.read_csv(FEATURES_PATH)

    # Quantile-based risk classification
    low_q = df["risk_score"].quantile(0.33)
    high_q = df["risk_score"].quantile(0.66)

    def risk_label(score):
        if score <= low_q:
            return "Low Risk"
        elif score <= high_q:
            return "Medium Risk"
        else:
            return "High Risk"

    df["risk_level"] = df["risk_score"].apply(risk_label)

    df.to_csv(FEATURES_PATH, index=False)

    print("✅ Risk levels assigned successfully!")
    print("Distribution:")
    print(df["risk_level"].value_counts())

if __name__ == "__main__":
    assign_risk_levels()
