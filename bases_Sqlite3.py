import pandas as pd
import sqlite3

# Configuraciones generales para distintos bots
data = [
    {
        "id": 1,
        "alyc": "InvertirOnline",
        "market": "MERV",
        "coneccion": "activa",
        "hora_inicio": "11",
        "hora_finalizacion": "17",
        "carpeta_de_datos": "C:/Users/thisi/OneDrive/Desktop/academic bots/datos/datos_bot_I",
        "id_datos_mercado": "/informacion_de_mercado",
        "id_datos_ordenes": "/informacion_de_ordenes"
    }
]

# Convertir a DataFrame
df_config = pd.DataFrame(data)

# Conectarse (o crear) a una base SQLite
conn = sqlite3.connect("config.db")

# Guardar el DataFrame en una tabla llamada 'config'
df_config.to_sql("config", conn, if_exists="replace", index=False)

# Cerrar conexión
conn.close()