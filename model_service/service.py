import bentoml
from bentoml.io import JSON
import joblib
import os

from pydantic import BaseModel

# Load model from mounted volume
MODEL_PATH = "model/clothing_classifier.pkl"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Did you copy it in?")

model = joblib.load(MODEL_PATH)

# Define input schema
class SingleInput(BaseModel):
    text: str

class BatchInput(BaseModel):
    texts: list[str]

svc = bentoml.Service("clothing_classifier")

@svc.api(input=JSON(pydantic_model=SingleInput), output=JSON())
def predict(body: SingleInput):
    return {"category": model.predict([body.text])[0]}

@svc.api(input=JSON(pydantic_model=BatchInput), output=JSON())
def batch_predict(body: BatchInput):
    return {"categories": model.predict(body.texts).tolist()}
