import pandas as pd
from pathlib import Path


def read_clean(file_path):
    # Identifica a extensão do arquivo usando pathlib
    file_extension = Path(file_path).suffix.lower()

    # Dicionário de funções de leitura do Pandas para diferentes tipos de arquivo
    read_extension = {
        '.csv': read_csv_clean,
        '.txt': read_csv_clean,
        '.xls': read_excel_clean,
        '.xlsx': read_excel_clean
        # Adicione mais extensões e funções de leitura conforme necessário
    }

    # Verifica se a extensão é suportada
    if file_extension not in read_extension:
        raise ValueError("Extensão do arquivo não suportada.")

    # Lê o arquivo usando a função correspondente à sua extensão
    df = read_extension[file_extension](file_path)

    return df
