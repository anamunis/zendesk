import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# Obter as credenciais do ambiente
email = 'SEU-EMAIL'
password_zendesk = 'SUA-SENHA'

secoes = ['NOME DA SEÇÃO']

def fetch_all_categories(secao):
    page = 1
    categories = []

    while True:
        url = f"https://{secao}.zendesk.com/api/v2/help_center/categories.json?page={page}"
        response = requests.get(url, auth=HTTPBasicAuth(email, password_zendesk))
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code != 200:
            print(f"Erro ao acessar a API: {response.status_code}")
            break

        response_data = response.json()
        
        # Verifica se a resposta tem a chave 'categories'
        if 'categories' not in response_data:
            break
        
        for category in response_data['categories']:
            category_dict = {
                'nome_ca': secao,
                'category_id': category['id'],
                'category_url': category['url'],
                'category_html_url': category['html_url'],
                'position': category['position'],
                'created_at': category['created_at'],
                'updated_at': category['updated_at'],
                'name': category['name'],
                'description': category['description'],
                'locale': category['locale'],
                'source_locale': category['source_locale'],
                'outdated': category['outdated']
            }
            categories.append(category_dict)
        
        # Verifica se há mais páginas
        if not response_data.get('next_page'):
            break
        
        page += 1
    
    return categories

# Coleta todas as categorias
all_categories = []
for secao in secoes:
    print(f"Coletando categorias da central de ajuda: {secao}")
    categories_produto = fetch_all_categories(secao)
    all_categories.extend(categories_produto)  # Adiciona as categorias coletadas à lista total

# Salva as categorias em um arquivo Excel
df = pd.DataFrame(all_categories)
df.to_excel(f'categorias.xlsx', index=False)

print("Categorias salvas em categorias.xlsx")