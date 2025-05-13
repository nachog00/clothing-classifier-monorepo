import bentoml
from bentoml.io import JSON
import joblib

model = joblib.load("model/clothing_classifier.pkl")

@bentoml.service()
class ClothingClassifier:
    @bentoml.api(input=JSON(), output=JSON())
    def predict(self, data):
        return {"category": model.predict([data['text']])[0]}

    @bentoml.api(input=JSON(), output=JSON())
    def batch_predict(self, data):
        return {"categories": model.predict(data['texts']).tolist()}
