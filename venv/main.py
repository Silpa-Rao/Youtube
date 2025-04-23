from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import joblib
import pandas as pd

class PredictionRequest(BaseModel):
    data: Dict[str, Any]

app = FastAPI(
    title="YouTube Earnings Prediction API",
    description="Predict yearly earnings from YouTube channel stats.",
    version="1.0.0",
)

# Load the pipeline
model = joblib.load("model_pipeline.pkl")

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        df = pd.DataFrame([request.data])
    except Exception as e:
        raise HTTPException(400, f"Invalid input: {e}")
    try:
        preds = model.predict(df)
    except Exception as e:
        raise HTTPException(500, f"Prediction failed: {e}")
    return {"predictions": preds.tolist()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
