###################################################################################################################################################################################
#                                                                             Português                                                                                           #
###################################################################################################################################################################################

# Copiar Artigos entre Subdomínios no Zendesk

Este script Python permite copiar artigos da Central de Ajuda de um subdomínio do Zendesk para outro. O script utiliza a API do Zendesk para buscar os dados do artigo no subdomínio de origem e criar uma cópia no subdomínio de destino.

### Funcionalidades

* Busca os dados do artigo (autor, título, corpo, permissões, etc.) do subdomínio de origem
* Cria uma cópia exata do artigo no subdomínio de destino dentro de uma seção específica
* Exibe mensagens de sucesso ou falha para cada artigo copiado

### Requisitos

* Python 3.x
* Biblioteca requests instalada
* Credenciais de acesso à API do Zendesk (e-mail e senha ou token)

### Como usar

* Configure as credenciais de autenticação: Substitua 'SEU-EMAIL' e 'SUA-SENHA' pelas suas credenciais da API do Zendesk
* Defina os subdomínios de origem e destino: Modifique as variáveis subdomain_origem e subdomain_destino com os subdomínios do Zendesk apropriados
* Liste os artigos a serem copiados: No formato ('ID DO ARTIGO', 'ID DA SEÇÃO DE DESTINO'), defina os artigos e suas seções de destino na variável tuples



###################################################################################################################################################################################
#                                                                               English                                                                                           #
###################################################################################################################################################################################

# Copy Articles Between Zendesk Subdomains

This Python script allows copying Help Center articles from one Zendesk subdomain to another. The script uses the Zendesk API to fetch the article data from the source subdomain and create a copy in the destination subdomain.

### Features

* Fetches article data (author, title, body, permissions, etc.) from the source subdomain
* Creates an exact copy of the article in the destination subdomain within a specific section
* Displays success or failure messages for each copied article

### Requirements

* Python 3.x
* requests library installed
* Zendesk API credentials (email and password or token)

### How to use

* Set up authentication credentials: Replace 'SEU-EMAIL' and 'SUA-SENHA' with your Zendesk API credentials
* Define the source and destination subdomains: Modify the subdomain_origem and subdomain_destino variables with the appropriate Zendesk subdomains
* List the articles to be copied: In the format ('ARTICLE ID', 'DESTINATION SECTION ID'), define the articles and their destination sections in the tuples variable