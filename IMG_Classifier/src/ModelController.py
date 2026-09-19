import os
import joblib
import sys

# IMPORTANTE: Aseguramos la ruta del proyecto en sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Si tu pipeline requiere la función de preprocesamiento del módulo local,
# importamos DataPreprocessing para que Pickle reconozca el contexto
try:
    from src.DataPreprocessing import DataPreprocessing
except ImportError:
    from DataPreprocessing import DataPreprocessing

try:
    from src.definitions import ROOT_DIR
except ModuleNotFoundError:
    from definitions import ROOT_DIR

#class ModelController:
#    def __init__(self):
#        self.model_path = os.path.join(ROOT_DIR, "resources", "models", "model.joblib")
#        if os.path.exists(self.model_path):
#            self.pipeline = joblib.load(self.model_path)
#        else:
#            self.pipeline = None
#
#    def predict(self, raw_text):
#        if self.pipeline is None:
#            raise ValueError("El modelo 'model.joblib' no fue encontrado.")
#        
#        # Como raw_text es un string recibido de la interfaz, 
#        # lo envolvemos en una lista para que el Pipeline lo procese en 2D [1, features]
#        if isinstance(raw_text, str):
#            raw_text = [raw_text]
#            
#        prediction = self.pipeline.predict(raw_text)
#        return prediction

class ModelController:
    def __init__(self):
        # Configuración de ruta robusta para local y Streamlit Cloud
        self.model_path = os.path.join(PROJECT_ROOT, "resources", "models", "model.joblib")
        
        if os.path.exists(self.model_path):
            self.pipeline = joblib.load(self.model_path)
        else:
            raise FileNotFoundError(f"No se encontró el modelo en: {self.model_path}")

    def predict(self, raw_text):
        if isinstance(raw_text, str):
            raw_text = [raw_text]
        return self.pipeline.predict(raw_text)
