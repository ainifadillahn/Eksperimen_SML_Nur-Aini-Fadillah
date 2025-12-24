import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, confusion_matrix, classification_report
from sklearn.model_selection import ParameterGrid
import mlflow
import mlflow.sklearn

mlflow.set_experiment("Machine_Failure_RF_Advance")

def main():
    train_df = pd.read_csv("ai4i2020_preprocessed/train.csv")
    test_df  = pd.read_csv("ai4i2020_preprocessed/test.csv")

    X_train = train_df.drop(columns=["Machine failure"])
    y_train = train_df["Machine failure"]

    X_test = test_df.drop(columns=["Machine failure"])
    y_test = test_df["Machine failure"]

    param_grid = {
        "n_estimators": [200],
        "max_depth": [None, 20],
        "min_samples_split": [2, 5]
    }

    for params in ParameterGrid(param_grid):
        with mlflow.start_run():
            # Log parameters
            for k, v in params.items():
                mlflow.log_param(k, v)

            model = RandomForestClassifier(
                random_state=42,
                **params
            )
            model.fit(X_train, y_train)

            y_proba = model.predict_proba(X_test)[:, 1]
            y_pred  = (y_proba >= 0.5).astype(int)

            roc_auc = roc_auc_score(y_test, y_proba)
            mlflow.log_metric("roc_auc", roc_auc)

            # ===== ARTEFAK 1: CONFUSION MATRIX =====
            cm = confusion_matrix(y_test, y_pred)
            plt.figure()
            plt.imshow(cm)
            plt.title("Confusion Matrix")
            plt.colorbar()
            plt.savefig("confusion_matrix.png")
            mlflow.log_artifact("confusion_matrix.png")

            # ===== ARTEFAK 2: FEATURE IMPORTANCE =====
            fi = pd.DataFrame({
                "feature": X_train.columns,
                "importance": model.feature_importances_
            }).sort_values(by="importance", ascending=False)

            fi.to_csv("feature_importance.csv", index=False)
            mlflow.log_artifact("feature_importance.csv")

            # ===== MODEL =====
            mlflow.sklearn.log_model(model, "model")

            print(f"ROC AUC: {roc_auc}")

if __name__ == "__main__":
    main()
