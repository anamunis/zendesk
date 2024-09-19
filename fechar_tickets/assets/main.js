document.addEventListener('DOMContentLoaded', function() {
    const client = ZAFClient.init();

    // Selecionando o botão e o modal
    const fecharTicketBtn = document.getElementById('fechar-ticket-btn');
    const modalConfirm = document.getElementById('modal-confirm');
    const confirmYes = document.getElementById('confirm-yes');
    const confirmNo = document.getElementById('confirm-no');

    // Exibe o modal ao clicar no botão "Fechar Ticket"
    fecharTicketBtn.addEventListener('click', function() {
        modalConfirm.style.display = 'flex';  // Exibe o modal de confirmação
    });

    // Ação ao clicar em "Sim" no modal
    confirmYes.addEventListener('click', function() {
        modalConfirm.style.display = 'none';  // Fecha o modal
        fecharTicket();  // Executa a função para fechar o ticket
    });

    // Ação ao clicar em "Não" no modal
    confirmNo.addEventListener('click', function() {
        modalConfirm.style.display = 'none';  // Fecha o modal sem fazer nada
    });

    // Função para fechar o ticket
    function fecharTicket() {
        client.get('ticket.id').then(function(ticketData) {
            const ticketId = ticketData['ticket.id'];

            const ticketUpdate = {
                "ticket": {
                    "status": "closed",
                    "comment": {
                        "body": "Ticket fechado com sucesso pelo aplicativo."
                    }
                }
            };

            client.request({
                url: `/api/v2/tickets/${ticketId}.json`,
                type: 'PUT',
                contentType: 'application/json',
                data: JSON.stringify(ticketUpdate),
            }).then(function(response) {
                // Sucesso: Adiciona o comentário de sucesso
                console.log('Ticket fechado com sucesso pelo app.');
            }).catch(function(error) {
                // Em caso de erro, adiciona o comentário com o erro
                const errorMessage = `Erro ao fechar o ticket: ${error.responseText}`;
                console.error(errorMessage);

                const errorComment = {
                    "ticket": {
                        "comment": {
                            "body": errorMessage
                        }
                    }
                };

                client.request({
                    url: `/api/v2/tickets/${ticketId}.json`,
                    type: 'PUT',
                    contentType: 'application/json',
                    data: JSON.stringify(errorComment),
                });
            });
        });
    }
});
