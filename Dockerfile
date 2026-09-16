# Usamos la imagen oficial completa de Python
FROM python:3.10

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos e instalamos las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la API y los dos archivos .pkl a la cápsula
COPY main.py .
COPY modelo_armonico_mensual.pkl .
COPY modelo_financiero_dc.pkl .

# Puerto por el que va a exponer la API el contenedor
EXPOSE 8000

# Comando para arrancar Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]