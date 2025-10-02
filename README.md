# Coletor de Notícias G1

Um script simples em Python que realiza Web Scraping para coletar e exibir as manchetes do dia do portal de notícias G1.

O projeto utiliza a biblioteca **requests** para fazer o download do conteúdo da página e a **BeautifulSoup** para analisar o HTML e extrair os dados desejados.

## 🚀 Requisitos

  - Python \>= 3.7
  - pip (gerenciador de pacotes do Python)
  - As bibliotecas listadas no arquivo `requirements.txt`

## ⚙️ Instalação

Siga os passos abaixo para configurar e preparar o ambiente para execução.

**1. Crie uma pasta para o projeto e adicione os arquivos:**

Primeiro, crie um diretório no seu computador e, dentro dele, salve os dois arquivos do projeto:

  - `coletor_noticias.py`
  - `requirements.txt`

**2. Abra o terminal e navegue até a pasta do projeto.**

**3. Crie e ative um Ambiente Virtual (Virtual Environment):**

É uma excelente prática isolar as dependências do projeto para evitar conflitos com outros projetos Python.

```bash
# Crie o ambiente virtual (isso criará uma pasta chamada 'venv')
python -m venv venv
```

Agora, ative o ambiente. O comando varia conforme o seu sistema operacional:

  - **Windows:**
    ```bash
    venv\Scripts\activate
    ```
  - **macOS / Linux:**
    ```bash
    source venv/bin/activate
    ```

Após a ativação, você verá `(venv)` no início da linha do seu terminal.

**4. Instale as dependências:**

Com o ambiente virtual ativo, instale as bibliotecas necessárias usando o `pip` e o arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

## ▶️ Execução

Para executar o script, certifique-se de que seu ambiente virtual `(venv)` está ativo e rode o seguinte comando:

```
python coletor_noticias.py
```

O terminal exibirá a lista de manchetes coletadas do portal G1.

## ✅ Funcionalidades

  - Lista as manchetes principais do portal de notícias G1.
  - Utiliza a biblioteca `requests` para baixar o conteúdo da web.
  - Utiliza a biblioteca `BeautifulSoup` para analisar o documento HTML.
  - Demonstra um exemplo prático de Web Scraping.
  - Estruturado para fácil entendimento e modificação.
  - Inclui tratamento básico de exceções para lidar com falhas de conexão.
