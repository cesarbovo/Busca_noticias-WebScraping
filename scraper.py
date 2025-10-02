import requests
from bs4 import BeautifulSoup

def coletar_manchetes_g1():
    """
    Realiza o web scraping da página inicial do G1.
    Retorna uma lista de dicionários, cada um com 'titulo' e 'link',
    ou uma string de erro em caso de falha.
    """
    url = 'https://g1.globo.com/'
    try:
        # Faz a requisição para a página
        response = requests.get(url, timeout=10)
        # Lança um erro se a requisição falhar (ex: status 404, 500)
        response.raise_for_status()

        # Analisa o HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')
        # Seleciona todos os elementos <a> com a classe 'feed-post-link'
        elementos_noticia = soup.select('.feed-post-link')

        if not elementos_noticia:
            return "Nenhum título de notícia foi encontrado com o seletor CSS."

        # Processa os dados encontrados
        noticias = []
        for noticia in elementos_noticia:
            titulo = noticia.text.strip()
            link = noticia.get('href') # Pega o atributo 'href' da tag <a>
            if titulo and link:
                noticias.append({'titulo': titulo, 'link': link})
        
        return noticias

    except requests.exceptions.RequestException as e:
        return f"Erro de conexão: Verifique sua internet. Detalhes: {e}"
    except Exception as e:
        return f"Um erro inesperado ocorreu durante o scraping: {e}"