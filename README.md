# Coletor de Notícias G1

Aplicação desktop com interface gráfica amigável que realiza Web Scraping para coletar e exibir as manchetes do dia do portal de notícias G1.

O projeto utiliza a biblioteca **requests** para fazer o download do conteúdo da página e a **BeautifulSoup** para analisar o HTML. A interface gráfica é construída com **Tkinter**, a biblioteca padrão do Python, e utiliza **threading** para garantir que a aplicação permaneça responsiva durante a coleta de dados.

## 🚀 Requisitos

  - Python \>= 3.7
  - pip (gerenciador de pacotes do Python)
  - As bibliotecas listadas no arquivo `requirements.txt`

## ⚙️ Instalação

Siga os passos abaixo para configurar e preparar o ambiente para execução.

**1. Crie uma pasta para o projeto e adicione os arquivos:**

Primeiro, crie um diretório no seu computador e, dentro dele, crie e salve os **três arquivos** do projeto:

  - `scraper.py` (contém a lógica de busca das notícias)
  - `main_app.py` (contém a interface gráfica e é o arquivo principal)
  - `requirements.txt` (lista as dependências externas)

**2. Abra o terminal e navegue até a pasta do projeto.**

**3. Crie e ative um Ambiente Virtual (Virtual Environment):**

Isso isola as dependências do projeto para evitar conflitos com outros projetos Python.

```bash
# Crie o ambiente virtual (isso criará uma pasta chamada 'venv')
python -m venv venv
```

Agora, ative o ambiente. O comando varia conforme o seu sistema operacional:

  - **Windows (PowerShell):**
    ```powershell
    # Pode ser necessário liberar a execução de scripts primeiro
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    venv\Scripts\activate
    ```
  - **Windows (CMD - Prompt de Comando):**
    ```bash
    venv\Scripts\activate.bat
    ```
  - **macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```

Após a ativação, você verá `(venv)` no início da linha do seu terminal.

**4. Instale as dependências:**

Com o ambiente virtual ativo, instale as bibliotecas necessárias usando o `pip`:

```bash
pip install -r requirements.txt
```

## ▶️ Execução

Para executar a aplicação, certifique-se de que seu ambiente virtual `(venv)` está ativo e rode o arquivo principal **`main_app.py`**:

```bash
python main_app.py
```

## ✅ Funcionalidades

  - Coleta e exibe as manchetes principais do portal de notícias G1.
  - Apresenta as notícias em uma interface gráfica amigável com Tkinter.
  - Inclui links clicáveis para cada notícia, que abrem no navegador padrão.
  - Utiliza `threading` para manter a interface responsiva durante a coleta de dados.
  - Código organizado em duas camadas: lógica de scraping (`scraper.py`) e apresentação (`main_app.py`).
  - Utiliza a biblioteca `requests` para baixar o conteúdo da web.
  - Utiliza a biblioteca `BeautifulSoup` para analisar o documento HTML.
