import pandas as pd
from pathlib import Path


def read_excel(file_path):
    # Lê o arquivo Excel e realiza o processamento específico para Excel
    df = pd.read_excel(file_path)

    # Se não houver a coluna 'Date', tenta encontrar a coluna 'time' e renomeá-la
    if 'Date' not in df.columns:
        if 'time' in df.columns:
            df.rename(columns={'time': 'Date'}, inplace=True)
        else:
            raise ValueError("Nenhuma coluna 'Date' ou 'time' encontrada no arquivo.")

    # Converte a coluna "Date" para datetime e usa como índice
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%Y-%m-%d %H:%M:%S')
    df.set_index('Date', inplace=True)

    # Convertendo a coluna 'Date' para conter apenas a data
    df.index = df.index.date

    # Remove NAs e NaNs
    df.dropna(inplace=True)

    # Ordena o DataFrame pelo índice (Data)
    df.sort_index(inplace=True)

    return df
