# 🏭 Data Center Digital Twin: Simulación Térmica y Financiera

API REST contenerizada que actúa como un gemelo digital para evaluar la viabilidad operativa (Free Cooling) y financiera de infraestructura crítica de Data Centers. 

El sistema fusiona modelado físico del clima con proyecciones financieras estocásticas para devolver métricas de negocio en tiempo real.

## 🚀 Arquitectura y Modelos

La API se apoya en una arquitectura de inferencia de baja latencia utilizando dos modelos pre-entrenados:
1. **Cerebro Físico (Regresión Armónica):** Utiliza Series de Fourier de primer orden para modelar la estacionalidad térmica continua de la región y determinar la activación de sistemas de Free Cooling.
2. **Cerebro Financiero (Surrogate Model):** Un modelo Random Forest destilado a partir de más de 60,000 iteraciones de Monte Carlo, entrenado para predecir dinámicamente el PUE, los costos energéticos y el margen bruto en base a la ocupación de racks y la temperatura.

## 🛠️ Stack Tecnológico
* **Backend:** FastAPI, Uvicorn, Pydantic.
* **Data Science:** Python, Scikit-Learn, NumPy, Joblib.
* **Despliegue:** Docker, Git.
