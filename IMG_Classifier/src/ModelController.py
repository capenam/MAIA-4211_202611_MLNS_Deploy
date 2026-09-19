import os
import sys
import joblib

# Configuración de rutas
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

class ModelController:
    def __init__(self):
        self.model_path = os.path.join(PROJECT_ROOT, "resources", "models", "model.joblib")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"No se encontró el archivo del modelo en: {self.model_path}")
        
        # Cargar el pipeline optimizado del GridSearchCV
        self.pipeline = joblib.load(self.model_path)

    def predict(self, raw_text):
        # Convertir a lista si entra un único string para que TfidfVectorizer lo procese
        if isinstance(raw_text, str):
            raw_text = [raw_text]
            
        # El Pipeline ejecuta TfidfVectorizer -> TruncatedSVD -> SGDClassifier
        return self.pipeline.predict(raw_text)