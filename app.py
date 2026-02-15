from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np

app = FastAPI()

bundle = joblib.load("final_oulad_pipeline.joblib")
model = bundle["model"]
threshold = bundle["threshold"]

expected_cols = list(model.named_steps["preprocess"].feature_names_in_)

@app.get("/")
def home():
    return {"message": "Dropout model API is running"}

@app.post("/predict")
def predict(data: dict):
    payload = data.get("data", data)
    df = pd.DataFrame([payload])
    df = df.reindex(columns=expected_cols, fill_value=np.nan)

    proba = float(model.predict_proba(df)[0, 1])
    pred = int(proba >= threshold)

    return {"probability": proba, "prediction": pred}