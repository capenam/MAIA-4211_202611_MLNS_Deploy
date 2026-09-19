import os
import joblib

try:
    from src.definitions import ROOT_DIR
except ModuleNotFoundError:
    from definitions import ROOT_DIR

class ModelController:
    def __init__(self):
        self.model_path = os.path.join(ROOT_DIR, "resources", "models", "model.joblib")
        if os.path.exists(self.model_path):
            self.pipeline = joblib.load(self.model_path)
        else:
            self.pipeline = None

    def predict(self, raw_text):
        if self.pipeline is None:
            raise ValueError("El modelo 'model.joblib' no fue encontrado.")
        
        # Como raw_text es un string recibido de la interfaz, 
        # lo envolvemos en una lista para que el Pipeline lo procese en 2D [1, features]
        if isinstance(raw_text, str):
            raw_text = [raw_text]
            
        prediction = self.pipeline.predict(raw_text)
        return prediction