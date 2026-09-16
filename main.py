import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Data Center Digital Twin - Añelo")

# 1. CARGAR LOS DOS CEREBROS
modelo_clima = joblib.load("modelo_armonico_mensual.pkl")
modelo_finanzas = joblib.load("modelo_financiero_dc.pkl")
#Dejas las rutas así por docker, porque crea un contenedor aislado
class EstadoDataCenter(BaseModel):
    mes: int = Field(..., ge=1, le=12)
    racks_alquilados: int = Field(..., ge=0, le=26)

@app.post("/digital-twin")
def evaluar_escenario(estado: EstadoDataCenter):
    # --- CONSULTA AL CEREBRO FÍSICO ---
    cos_val = np.cos(2 * np.pi * estado.mes / 12)
    sin_val = np.sin(2 * np.pi * estado.mes / 12)
    temp_estimada = float(modelo_clima.predict(np.array([[cos_val, sin_val]]))[0])
    
    # --- CONSULTA AL CEREBRO FINANCIERO ---
    pred_finanzas = modelo_finanzas.predict(np.array([[estado.mes, estado.racks_alquilados]]))[0]
    pue_esperado = pred_finanzas[0]
    ingresos = pred_finanzas[1]
    costos = pred_finanzas[2]

    # --- RESPUESTA CONSOLIDADA ---
    return {
        "entorno_ambiental": {
            "mes": estado.mes,
            "temperatura_media_c": round(temp_estimada, 2),
            "free_cooling_recomendado": temp_estimada <= 18.0
        },
        "proyeccion_negocio": {
            "racks_activos": estado.racks_alquilados,
            "pue_estimado": round(pue_esperado, 3),
            "ingresos_usd": round(ingresos, 2),
            "costos_energia_usd": round(costos, 2),
            "margen_bruto_usd": round(ingresos - costos, 2)
        }
    }