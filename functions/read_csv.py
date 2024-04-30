import pandas as pd
from pathlib import Path


def read_csv(file_path):
    # Lê o arquivo CSV e realiza o processamento específico para CSV
    df = pd.read_csv(file_path)

    # Separa as colunas Date e Adj Close, se necessário
    if ';' in df.columns[0]:
        df[['Date', 'Adj Close']] = df.iloc[:, 0].str.split(';', expand=True)
        df.drop(columns=[df.columns[0]], inplace=True)

    # Converte a coluna "Date" para datetime e usa como índice
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%d/%m/%Y')
        df.set_index('Date', inplace=True)
    else:
        raise ValueError("Nenhuma coluna 'Date' encontrada no arquivo.")

    # Remove NAs e NaNs
    df.dropna(inplace=True)

    # Ordena o DataFrame pelo índice (Data)
    df.sort_index(inplace=True)

    return df
