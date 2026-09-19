import streamlit as st
import sys
import os
st.set_page_config(page_title="Clasificador ODS", page_icon="🌱", layout="wide")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ModelController import ModelController
from src.DataPreprocessing import DataPreprocessing

@st.cache_resource
def load_controller():
     return ModelController()

model_controller = load_controller()
preprocessor = DataPreprocessing()

st.title("🌱 Clasificador de Opiniones Ciudadanas según ODS (Agenda 2030)")
st.write("Ingresa un texto o propuesta ciudadana para identificar su relación semántica con los ODS [1, 2].")

user_text = st.text_area("Ingresa la propuesta ciudadana:", height=150)


if st.button("🔍 Clasificar ODS", type="primary"):
    if user_text.strip():
        # 1. Obtenemos el resultado de la predicción
        pred = model_controller.predict(user_text)
        
        # Extraemos el valor del arreglo/lista si es necesario
        ods_pred = pred[0] if hasattr(pred, "__getitem__") else pred
        
        # Convertimos a entero para buscar en el diccionario de ODS
        ods_key = int(ods_pred)
        
        # 2. Obtenemos la información de la clase
        info = preprocessor.get_ods_info(ods_key)

        # 3. Renderizamos el resultado
        st.markdown(f"""
        <div style="background-color: {info.get('color', '#1F2937')}; padding: 20px; border-radius: 10px; color: white;">
            <h2>{info.get('icono', '🌱')} ODS {ods_key}: {info.get('nombre', 'Clasificado')}</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Ingresa un texto antes de clasificar.")