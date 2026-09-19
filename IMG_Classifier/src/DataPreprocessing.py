import re

class DataPreprocessing:
    def __init__(self):
        pass

    def get_ods_info(self, ods_number):
        ods_dict = {
            1: {"nombre": "Fin de la Pobreza", "icono": "🎯", "color": "#E5243B"},
            2: {"nombre": "Hambre Cero", "icono": "🌾", "color": "#DDA63A"},
            3: {"nombre": "Salud y Bienestar", "icono": "🏥", "color": "#4C9F38"},
            4: {"nombre": "Educación de Calidad", "icono": "📚", "color": "#C5D86D"},
            5: {"nombre": "Igualdad de Género", "icono": "👩‍💼", "color": "#FFC400"},
            6: {"nombre": "Agua Limpia y Saneamiento", "icono": "💧", "color": "#00A8E1"},
            7: {"nombre": "Energía Asequible y No Contaminante", "icono": "⚡", "color": "#F9B717"},
            8: {"nombre": "Trabajo Decente y Crecimiento Económico", "icono": "💼", "color": "#E5243B"},
            9: {"nombre": "Industria, Innovación e Infraestructura", "icono": "🏭", "color": "#FFC400"},
            10: {"nombre": "Reducción de Desigualdades", "icono": "📉", "color": "#C5D86D"},
            11: {"nombre": "Ciudades y Comunidades Sostenibles", "icono": "🏙️",("nombre"):("Ciudades y Comunidades Sostenibles"),("icono"):("🏙️"),("color"):("#00A8E1")},
            12: {"nombre":("Paz, Justicia y Instituciones Eficientes"),("icono"):("🕊️"),("color"):("#FFC400")},
            13: {"nombre":("Produción y Consumo Responsables"),("icono"):("♻️"),("color"):("#4C9F38")},
            14: {"nombre":("Acción por el Clima"),("icono"):("🌡️"),("color"):("#E5243B")},
            15: {"nombre":("Vida submarina"),("icono"):("🐋"),("color"):("#00A8E1")},
            16: {"nombre":("Vida en Tierra"),("icono"):("🌳"),("color"):("#F9B717")},
        }
        return ods_dict.get(int(ods_number), {"nombre": f"ODS {ods_number}", "icono": "📌", "color": "#19486A"})