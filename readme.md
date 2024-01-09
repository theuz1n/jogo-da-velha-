
# tictactoe


 O projeto tem como objetivo fazer uma implementação do jogo da velha de forma distribuída onde cada jogador estará numa máquina, com sua própria visão do jogo, tendo suas jogadas enviadas via rede.

Para os propósitos desta aplicação podemos definir que o Cliente será sempre o jogador X ao passo que o Servidor será sempre o O.

A aplicação é desenvolvida para trabalhar os seguintes conceitos em python com redes.

- udp 

- tcp

- módulos pickle e struct usados para transmissão de dados


### **Implementação do projeto**

### Cliente:

- Ao iniciar, o cliente procura automaticamente o servidor na rede utilizando o método de Broadcast.
- Após encontrar o servidor, o cliente estabelece uma conexão para aceitar datagramas apenas do servidor.
- O jogo inicia quando o cliente recebe uma mensagem de autorização do servidor, como por exemplo, "START".
- A partida continua até que um dos jogadores vença ou termine em empate.
- Após o término do jogo, o cliente encerra e para uma nova partida é necessário iniciar um novo cliente.

### Servidor:

- Ao ser iniciado, o servidor espera ser descoberto por um cliente.
- Uma vez descoberto, o servidor envia uma mensagem de confirmação, como por exemplo, "HELLO".
- Após isso, o servidor prepara o cliente para o início do jogo enviando uma mensagem "START".
- Ambos, cliente e servidor, reiniciam as variáveis do jogo para a próxima partida.
- O servidor permanece em execução indefinidamente, aguardando a descoberta de um novo cliente após o término de cada partida.

## Execução

1. **Cliente:**
    
    - Execute o cliente para encontrar automaticamente o servidor na rede.
    - Aguarde a autorização do servidor para iniciar a partida.
    - Jogue até que um vencedor seja determinado ou a partida termine em empate.
    - Encerre o cliente para finalizar a partida.
2. **Servidor:**
    
    - Inicie o servidor e aguarde a descoberta por parte de um cliente.
    - Após a descoberta, envie a mensagem de confirmação e prepare o cliente para o jogo.
    - Continue executando para receber novos clientes e iniciar novas partidas.

## Observações

- Certifique-se de que as variáveis do jogo sejam reiniciadas corretamente para cada nova partida.
- O ciclo do servidor se repete, esperando por novos clientes após o término de cada partida.

Divirta-se jogando e explorando a dinâmica deste simples jogo de conexão Cliente-Servidor!
