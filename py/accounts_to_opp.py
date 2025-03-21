import pandas as pd
import os

# Definir rutas
csv_folder = os.path.join(os.getcwd(), "csv")
output_folder = os.path.join(os.getcwd(), "csvcorregidos")
account_file = os.path.join(csv_folder, "Account_Clean.csv")
opportunity_file = os.path.join(csv_folder, "Opportunities_Clean.csv")
output_file = os.path.join(output_folder, "Opportunities_Clean_Corregido.csv")

# Asegurar que la carpeta de salida exista
os.makedirs(output_folder, exist_ok=True)

try:
    # Cargar Account_Clean.csv
    account_df = pd.read_csv(account_file)

    # Mostrar columnas reales del archivo
    print("📌 Columnas encontradas en Account_Clean.csv:", account_df.columns.tolist())

    # Intentar detectar los nombres correctos de columnas
    posibles_columnas = ["Account_ID", "Accounts_ID Name"]
    columnas_presentes = [col for col in posibles_columnas if col in account_df.columns]

    if len(columnas_presentes) < 2:
        raise ValueError(f"❌ Error en la estructura del CSV: No se encontraron ambas columnas necesarias en Account_Clean.csv. "
                         f"Columnas detectadas: {account_df.columns.tolist()}")

    # Renombrar las columnas clave para evitar problemas
    account_df = account_df.rename(columns={
        "Account_ID": "Account_ID",
        "Accounts_ID Name": "Accounts_ID"
    })

    # Cargar Opportunities_Clean.csv
    opportunity_df = pd.read_csv(opportunity_file)

    # Reemplazar Account_ID por Accounts_ID
    merged_df = opportunity_df.merge(account_df[["Account_ID", "Accounts_ID"]], on="Account_ID", how="left")
    merged_df = merged_df.drop(columns=["Account_ID"]).rename(columns={"Accounts_ID": "Account_ID"})

    # Guardar el archivo corregido
    merged_df.to_csv(output_file, index=False)
    print(f"✅ Archivo corregido guardado en: {output_file}")

except FileNotFoundError as e:
    print(f"❌ Error: No se encontró el archivo. Verifica que está en la carpeta correcta. \nDetalles: {e}")
except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")
