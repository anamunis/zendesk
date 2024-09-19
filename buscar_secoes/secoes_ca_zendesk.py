import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# Obter as credenciais do ambiente
email = 'SEU-EMAIL'
senha = 'SUA-SENHA'

secoes = ['NOME DA SEÇÃO']

def fetch_all_sections(secao):
    page = 1
    sections = []

    while True:
        url = f"https://{secao}.zendesk.com/api/v2/help_center/sections.json?page={page}"
        response = requests.get(url, auth=HTTPBasicAuth(email, senha))
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code != 200:
            print(f"Erro ao acessar a API: {response.status_code}")
            break

        response_data = response.json()
        
        # Verifica se a resposta tem a chave 'sections'
        if 'sections' not in response_data:
            break
        
        for section in response_data['sections']:
            section_dict = {
                'nome_ca': secao,
                'section_id': section['id'],
                'section_url': section['url'],
                'section_html_url': section['html_url'],
                'position': section['position'],
                'sorting': section['sorting'],
                'created_at': section['created_at'],
                'updated_at': section['updated_at'],
                'name': section['name'],
                'description': section['description'],
                'locale': section['locale'],
                'source_locale': section['source_locale'],
                'outdated': section['outdated'],
                'parent_section_id': section['parent_section_id'],
                'theme_template': section['theme_template']
            }
            sections.append(section_dict)
        
        # Verifica se há mais páginas
        if not response_data.get('next_page'):
            break
        
        page += 1
    
    return sections

# Coleta todas as seções
all_sections = []
for secao in secoes:
    print(f"Coletando seções da central de ajuda: {secao}")
    sections_produto = fetch_all_sections(secao)
    all_sections.extend(sections_produto)  # Adiciona as seções coletadas à lista total

# Salva as seções em um arquivo Excel
df = pd.DataFrame(all_sections)
df.to_excel(f'secoes.xlsx', index=False)

print("Seções salvas em secoes.xlsx")