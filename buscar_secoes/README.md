###################################################################################################################################################################################
#                                                                             Português                                                                                           #
###################################################################################################################################################################################

# Coletar Seções da Central de Ajuda do Zendesk

Este script Python coleta todas as seções da Central de Ajuda de um ou mais subdomínios do Zendesk usando a API do Zendesk e armazena as informações em um arquivo Excel. Cada seção contém dados como ID, URLs, posição, idioma, entre outros.

### Funcionalidades

* Consulta todas as seções de um ou mais subdomínios do Zendesk
* Coleta detalhes de cada seção, como ID, URL, nome, descrição, idioma, etc
* Exporta os dados coletados para um arquivo Excel

### Requisitos

* Python 3.x
* Bibliotecas requests e pandas instaladas
* Credenciais de acesso à API do Zendesk (e-mail e senha ou token)

### Como usar

* Configurar credenciais: Substitua 'SEU-EMAIL' e 'SUA-SENHA' pelas suas credenciais da API do Zendesk
* Configurar as seções: Na lista secoes, substitua 'NOME DA SEÇÃO' pelos nomes dos subdomínios Zendesk que deseja consultar



###################################################################################################################################################################################
#                                                                               English                                                                                           #
###################################################################################################################################################################################

# Fetch Zendesk Help Center Sections

This Python script collects all sections from the Help Center of one or more Zendesk subdomains using the Zendesk API and stores the information in an Excel file. Each section contains data such as ID, URLs, position, language, and more.

### Features

* Fetches all sections from one or more Zendesk subdomains
* Collects details for each section, such as ID, URL, name, description, language, etc
* Exports the collected data to an Excel file

### Requirements

* Python 3.x
* requests and pandas libraries installed
* Zendesk API credentials (email and password or token)

### How to use

* Set up authentication credentials: Replace 'SEU-EMAIL' and 'SUA-SENHA' with your Zendesk API credentials
* Configure the sections: In the secoes list, replace 'NOME DA SEÇÃO' with the names of the Zendesk subdomains you want to query.