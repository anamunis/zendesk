document.addEventListener('DOMContentLoaded', function () {
    const client = ZAFClient.init();

    // Selecionando o botão e o campo de texto
    const clonarTicketBtn = document.getElementById('clonar-ticket-btn');
    const novoTituloInput = document.getElementById('novo-titulo');

    // Pega o título e executa a função ao clicar no botão "Clonar Ticket"
    clonarTicketBtn.addEventListener('click', function () {
        const novoTitulo = novoTituloInput.value.trim();
        clonarTicket(novoTitulo);  // Executa a função para clonar o ticket
    });

    function clonarTicket(novoTitulo) {
        // Obtém os dados básicos do ticket atual
        client.get('ticket').then(function (ticketData) {
            const ticket = ticketData.ticket;

            // Log dos dados básicos do ticket
            console.log('ticketData:', JSON.stringify(ticket, null, 2));

            // Faz uma requisição completa ao Zendesk para obter todos os detalhes do ticket
            client.request({
                url: `/api/v2/tickets/${ticket.id}.json`,
                type: 'GET',
                contentType: 'application/json',
            }).then(function (response) {
                const ticketJson = response.ticket;

                // Log dos dados completos do ticket
                console.log('ticketJson:', JSON.stringify(ticketJson, null, 2));

                // Armazena os valores dos campos em variáveis
                const requesterId = ticket.requester ? ticket.requester.id : null;
                const assigneeId = ticket.assignee && ticket.assignee.user ? ticket.assignee.user.id : null;
                const priority = ticket.priority;
                const ticketFormId = ticket.form ? ticket.form.id : null;

                // Mensagem de comentário para o novo ticket
                const internalComment = `Ticket criado a partir dos dados do ticket ${ticketJson.id}`;

                // Obtém os campos customizados do ticket
                const customFields = ticketJson.custom_fields || [];

                // Copia apenas os campos customizados que têm valor
                const customFieldsToCopy = customFields.filter(field => field.value !== null && field.value !== "");

                // Cria um novo ticket com base nos dados do ticket atual
                const newTicket = {
                    "ticket": {
                        "subject": novoTitulo,  // Usa o título fornecido pelo agente
                        "ticket_form_id": ticketFormId, // Adiciona o form_id do ticket
                        "comment": {
                            "body": internalComment,
                            "public": false  // Comentário interno
                        },
                        "priority": priority,
                        "status": "new",
                        "assignee_id": assigneeId,
                        "requester_id": requesterId,
                        "custom_fields": customFieldsToCopy  // Copia os campos customizados com valor
                    }
                };

                // Faz uma requisição para criar o novo ticket
                client.request({
                    url: '/api/v2/tickets.json',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify(newTicket),
                }).then(function (response) {
                    const newTicketId = response.ticket.id;

                    // Adiciona um comentário ao ticket original informando sobre a criação do novo ticket
                    const ticketUpdate = {
                        "ticket": {
                            "comment": {
                                "body": `O ticket ${newTicketId} foi criado com sucesso.`,
                                "public": false  // Comentário interno no ticket original também
                            }
                        }
                    };

                    client.request({
                        url: `/api/v2/tickets/${ticket.id}.json`,
                        type: 'PUT',
                        contentType: 'application/json',
                        data: JSON.stringify(ticketUpdate),
                    }).then(function () {
                        console.log(`Ticket ${newTicketId} criado com sucesso.`);

                        // Abrir o novo ticket em uma nova aba no Zendesk
                        client.invoke('routeTo', 'ticket', newTicketId);
                    });
                }).catch(function (error) {
                    console.error('Erro ao criar o novo ticket: ', error);
                });
            }).catch(function (error) {
                console.error('Erro ao obter dados do ticket atual: ', error);
            });
        });
    }
});
