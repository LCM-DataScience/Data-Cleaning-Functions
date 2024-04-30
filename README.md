**Funções de Leitura e Limpeza:**

  Este projeto contém três módulos, cada um definindo uma função específica para ler e tratar diferentes tipos de arquivos: CSV, TXT e Excel.
  Cada função (read_csv, read_txt e read_excel) aceita um caminho de arquivo como entrada e retorna um DataFrame do Pandas com os dados lidos e limpos.


**Função Principal de Leitura:**

  O arquivo 'read_clean.py' define a função 'read_clean', que identifica a extensão do arquivo e chama a função de leitura correspondente no módulo apropriado.
  Esta função permite ler arquivos com extensões .csv, .txt, .xls e .xlsx, garantindo que os dados sejam lidos e realizados os 'Data Cleansing' iniciais como "dropna"
  e especificamente tratadas as colunas "Data" convertidas para "dtype('<M8[ns] / datetime64[ns]".


**Exemplo de Uso:**

  O arquivo 'main_auto_clean.ipynb' importa as funções de leitura específicas do arquivo functions.
  Temos dois exemplos de uso com um arquivo CSV e outro Excel, recebendo os tratamentos das funções definidas nos arquivos '.py'.

**Execução do Código:**

  O código pode ser executado em um ambiente Python, Jupyter Notebook, VS Code ou de sua preferência, desde que todas as dependências estejam instaladas e as configurações de ambiente estejam corretas.
  Certifique-se de ajustar os caminhos onde os arquivos que deseja tratar estão salvos em seu sistema.


🎯


Gostaria de deixar comentários, críticas ou sugestões?
Entre em contato pelo email jobs.luis78@gmail.com 😉
