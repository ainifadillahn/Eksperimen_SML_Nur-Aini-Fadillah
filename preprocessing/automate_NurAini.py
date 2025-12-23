import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os


def preprocess_data(input_path, output_dir):
    # Load data
    df = pd.read_csv(input_path)

    # Drop kolom sesuai notebook
    X = df.drop(columns=[
        "UDI",
        "Product ID",
        "Type",
        "Machine failure",
        "TWF", "HDF", "PWF", "OSF", "RNF"
    ])
    y = df["Machine failure"]

    # Train-test split (sama seperti notebook)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Scaling (FIT hanya di train)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Kembalikan ke DataFrame
    train_df = pd.DataFrame(X_train_scaled, columns=X.columns)
    train_df["Machine failure"] = y_train.values

    test_df = pd.DataFrame(X_test_scaled, columns=X.columns)
    test_df["Machine failure"] = y_test.values

    # Buat folder output jika belum ada
    os.makedirs(output_dir, exist_ok=True)

    # Simpan hasil preprocessing
    train_df.to_csv(f"{output_dir}/train.csv", index=False)
    test_df.to_csv(f"{output_dir}/test.csv", index=False)


if __name__ == "__main__":
    preprocess_data(
        input_path="ai4i_raw/ai4i2020.csv",
        output_dir="preprocessing/ai4i2020_preprocessed"
    )
