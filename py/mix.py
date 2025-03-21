import os
import pandas as pd
import random

# Definir rutas
input_folder = "csvcorregidos"  # Carpeta con los archivos originales
output_folder = "csvcorregidos_reducidos"  # Carpeta donde se guardarán los archivos reducidos

# Asegurar que la carpeta de salida exista
os.makedirs(output_folder, exist_ok=True)

# Lista de archivos esperados
files = {
    "Accounts_Clean": "Accounts_Clean .csv",
    "Cases_Clean": "Cases_Clean.csv",
    "Contacts_Clean": "Contacts_Clean.csv",
    "Opportunities_Clean": "Opportunities_Clean.csv"
}

# Cargar todos los archivos en dataframes
dataframes = {key: pd.read_csv(os.path.join(input_folder, filename)) for key, filename in files.items()}

# Extraer todos los Account_ID únicos presentes en los archivos secundarios
all_account_ids = set(dataframes["Accounts_Clean"]["Account_ID"])
for key in ["Cases_Clean", "Contacts_Clean", "Opportunities_Clean"]:
    all_account_ids &= set(dataframes[key]["Account_ID"])  # Mantener solo IDs comunes

# Reducir la cantidad de Account_IDs al 50%
selected_accounts = set(random.sample(list(all_account_ids), len(all_account_ids) // 2))

# Función para filtrar datos basados en Account_ID
def filter_data(df):
    return df[df["Account_ID"].isin(selected_accounts)]

# Aplicar la reducción manteniendo relaciones
for key, df in dataframes.items():
    reduced_df = filter_data(df)
    output_path = os.path.join(output_folder, files[key])
    reduced_df.to_csv(output_path, index=False)  # Guardar archivo reducido
    print(f"Archivo reducido guardado: {files[key]}")

print("✅ Proceso completado. Todos los archivos están relacionados correctamente.")
