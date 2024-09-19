import requests
from requests.auth import HTTPBasicAuth
import json
import re

# Credenciais de autenticação
email = 'SEU-EMAIL'
senha = 'SUA-SENHA'

def copy_articles(email, senha, tuples):
    for article_id, section_id_destino in tuples:
        # URL para o artigo no subdomínio de origem
        url_origem = f'https://{subdomain_origem}.zendesk.com/api/v2/help_center/articles/{article_id}.json'
        
        # URL para criar o artigo no subdomínio de destino
        url_destino = f'https://{subdomain_destino}.zendesk.com/api/v2/help_center/sections/{section_id_destino}/articles.json'
        
        # Dados do artigo no subdomínio de origem
        response_origem = requests.get(url_origem, auth=HTTPBasicAuth(email, senha))
        if response_origem.status_code == 200:
            article_data = response_origem.json()['article']
            article_author = article_data['author_id']
            article_name = article_data['name']
            article_title = article_data['title']
            article_body = article_data['body']
            article_source_locale = article_data['source_locale']
            article_locale = article_data['locale']
            article_permission = article_data['permission_group_id']


        else:
            print(f"Falha ao obter dados do artigo do subdomínio de origem. Código de status: {response_origem.status_code}")
            continue
        
        # Criando uma cópia do artigo no subdomínio de destino
        data_destino = {
            "article": {
                "author_id": article_author,
                "section_id": section_id_destino,
                "name": article_name,
                "title": article_title,
                "source_locale": article_source_locale,
                "locale": article_locale,
                "user_segment_id": None,
                "permission_group_id": article_permission,
                "body": article_body
            },
            "notify_subscribers": False
        }
        
        headers = {'Content-Type': 'application/json'}
        
        response_destino = requests.post(url_destino,
                                          auth=HTTPBasicAuth(email, senha),
                                          headers=headers,
                                          data=json.dumps(data_destino))
        
        if response_destino.status_code == 201:
            new_article_id = response_destino.json()['article']['id']
            print(f"Artigo copiado com sucesso para o subdomínio de destino. Novo ID do artigo: {new_article_id}")
        else:
            print(f"Falha ao criar o artigo {article_id} no subdomínio de destino. Código de status: {response_destino.status_code}")
            print("Resposta:", response_destino.text)


subdomain_origem = 'SUBDOMINIO-ORIGEM'
subdomain_destino = 'SUBDOMINIO-DESTINO'
tuples = [('ID DO ARTIGO', 'ID DA SEÇÃO DE DESTINO')]


copy_articles(email, senha, tuples)