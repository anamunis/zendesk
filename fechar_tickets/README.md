###################################################################################################################################################################################
#                                                                             Português                                                                                           #
###################################################################################################################################################################################

# Fechar Ticket

Este aplicativo foi desenvolvido para funcionar dentro do Zendesk, permitindo que os agentes fechem um ticket diretamente da interface do ticket.

### Funcionalidades

* Fecha automaticamente o ticket em que o usuário está trabalhando
* Exibe um modal de confirmação antes de fechar o ticket
* Adiciona um comentário ao ticket e ao log do console confirmando o fechamento com sucesso
* Em caso de erro, registra o erro como um comentário no ticket

### Requisitos

* Zendesk Support com permissões de gerenciamento de tickets

### Interface

* O botão "Fechar Ticket" é centralizado horizontalmente e posicionado na parte inferior da tela do aplicativo
* O modal de confirmação é exibido com os botões "Sim" e "Não":
    * Sim: Fecha o ticket e adiciona um comentário de confirmação
    * Não: Fecha o modal sem realizar nenhuma ação



###################################################################################################################################################################################
#                                                                               English                                                                                           #
###################################################################################################################################################################################

# Close Ticket

This application was developed to work within Zendesk, allowing agents to close a ticket directly from the ticket interface.

### Features

* Automatically closes the ticket the user is working on
* Displays a confirmation modal before closing the ticket
* Adds a comment to the ticket and logs a confirmation of the successful closure in the console
* In case of an error, logs the error as a comment on the ticket

### Requirements

* Zendesk Support with ticket management permissions

### Interface

* The "Close Ticket" button is horizontally centered and positioned at the bottom of the app screen
* The confirmation modal is displayed with "Yes" and "No" buttons:
    * Yes: Closes the ticket and adds a confirmation comment
    * No: Closes the modal without performing any action