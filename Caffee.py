import pandas as pd
import numpy as np
from sqlalchemy import create_engine

df=pd.read_csv(r"C:\Users\Kenzo\Documents\Visual Studio Code\Data cleaning\dirty_cafe_sales.csv")


print(df.columns) #Para ver los titulos como estàn escritos.


df["Item"]=df["Item"].replace(["UNKNOWN","ERROR","nan"],np.nan)
df = df.dropna(subset=["Item"])
print(df["Item"].unique())

df["Quantity"]=df["Quantity"].replace(["UNKNOWN","ERROR","nan"],np.nan)
df = df.dropna(subset=["Quantity"])
df["Quantity"] = df["Quantity"].astype(int)
print(df["Quantity"].unique())

df["Price Per Unit"]=df["Price Per Unit"].replace(["UNKNOWN","ERROR","nan"],np.nan)
df = df.dropna(subset=["Price Per Unit"])
df["Price Per Unit"] = df["Price Per Unit"].astype(float)
print(df["Price Per Unit"].unique())

avg_prices = df.groupby("Item")["Price Per Unit"].mean().to_dict()
print(avg_prices)

df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Item"].map(avg_prices))
print(df["Price Per Unit"].unique())


df["Total Spent"]=df["Total Spent"].replace(["UNKNOWN","ERROR","nan"],np.nan)
df["Total Spent"]=df["Total Spent"].fillna(df["Quantity"]*df["Price Per Unit"])
df["Total Spent"]=df["Total Spent"].astype(float)
print(df["Total Spent"].unique())


df["Payment Method"]=df["Payment Method"].replace(["UNKNOWN","ERROR","nan"],np.nan)
print(df["Payment Method"].unique())
df["Location"]=df["Location"].replace(["UNKNOWN","ERROR","nan"],np.nan)
print(df["Location"].unique())
df["Transaction Date"]=df["Transaction Date"].replace(["UNKNOWN","ERROR","nan"],np.nan)

df["Transaction Date"]=pd.to_datetime(df["Transaction Date"])
df["Mes"] = df["Transaction Date"].dt.month_name()

# Datos de conexión
usuario = "postgres"
contraseña = "Daksol50PA#"
host = "localhost"   # o la IP del servidor
puerto = "5432"      # puerto por defecto de PostgreSQL
db = "postgres"

# Crear engine de SQLAlchemy
engine = create_engine(f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{db}")

df.to_sql(
    "postgres",           # nombre de la tabla en PostgreSQL
    engine,
    if_exists="replace",  # reemplaza la tabla si ya existe
    index=False           # no guarda el índice de pandas
)

df_sql = pd.read_sql("SELECT * FROM postgres LIMIT 5", engine)
print(df_sql)

