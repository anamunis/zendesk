import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# Obter as credenciais do ambiente
email = 'SEU-EMAIL'
password_zendesk = 'SUA-SENHA'

secoes = ['NOME DA SEÇÃO']

def fetch_all_articles(secao):
    page = 1
    articles = []

    while True:
        url = f"https://{secao}.zendesk.com/api/v2/help_center/articles.json?page={page}"
        response = requests.get(url, auth=HTTPBasicAuth(email, password_zendesk))
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code != 200:
            print(f"Erro ao acessar a API: {response.status_code}")
            break

        response_data = response.json()
        
        # Verifica se a resposta tem a chave 'categories'
        if 'articles' not in response_data:
            break
        
        for article in response_data['articles']:
            article_dict = {
                'nome_ca': secao,
                'article_id': article['id'],
                'article_url': article['url'],
                'article_html_url': article['html_url'],
                'author_id': article['author_id'],
                'comments_disabled': article['comments_disabled'],
                'promoted': article['promoted'],
                'position': article['position'],
                'vote_sum': article['vote_sum'],
                'vote_count': article['vote_count'],
                'section_id': article['section_id'],
                'created_at': article['created_at'],
                'updated_at': article['updated_at'],
                'name': article['name'],
                'title': article['title'],
                'locale': article['locale'],
                'source_locale': article['source_locale'],
                'outdated': article['outdated'],
                'outdated_locales': article['outdated_locales'],
                'edited_at': article['edited_at'],
                'user_segment_id': article['user_segment_id'],
                'permission_group_id': article['permission_group_id'],
                'content_tag_ids': article['content_tag_ids'],
                'label_names': article['label_names'],
                'body': article['body']
            }
            articles.append(article_dict)
        
        # Verifica se há mais páginas
        if not response_data.get('next_page'):
            break
        
        page += 1
    
    return articles

# Coleta todas os artigos
all_articles = []
for secao in secoes:
    print(f"Coletando artigos da central de ajuda: {secao}")
    articles_secao = fetch_all_articles(secao)
    all_articles.extend(articles_secao)  # Adiciona os artigos coletados à lista total

# Salva os artigos em um arquivo Excel
df = pd.DataFrame(all_articles)
df.to_excel(f'artigos.xlsx', index=False)

print("Artigos salvos em artigos.xlsx")