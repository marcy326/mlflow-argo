import argparse
import mlflow
import mlflow.sklearn
import joblib

def main(parent_run_id):
    with mlflow.start_run(run_id=parent_run_id, nested=True) as run:
        # モデルの読み込み
        model = mlflow.sklearn.load_model(f"runs:/{parent_run_id}/random_forest_model")
        
        # モデルの保存
        joblib.dump(model, "/mnt/mlflow-project/model/random_forest_model.pkl")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent_run_id", type=str, required=True)
    args = parser.parse_args()
    main(args.parent_run_id)
