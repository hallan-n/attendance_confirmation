# Attendance Confirmation

## Descrição
Este projeto é uma aplicação para confirmação de presença no meu casamento. Ele permite que os organizadores de eventos gerenciem a lista de participantes e que os convidados confirmem sua presença.

## Funcionalidades
- Cadastro de eventos
- Gerenciamento de lista de participantes
- Gerenciamento de lista de presentes
- Confirmação de presença por parte dos convidados
- Envio de notificações p# Attendance Confirmation

## Tecnologias Utilizadas
- Linguagem de Programação: Python
- Framework: FastAPI, SQLModel
- Banco de Dados: MySQL, SQLite

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/hallan-n/attendance_confirmation.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd attendance_confirmation
    ```
3. Construa a imagem Docker:
    ```bash
    make build
    ```

## Uso
1. Inicie o container:
    ```bash
    make run
    ```
2. Acesse a aplicação no navegador:
    ```
    http://localhost:8000/docs
    ```

## Comandos Disponíveis no Makefile
- **`make build`**: Constrói a imagem Docker do projeto.
- **`make run`**: Inicia o container Docker em modo detached.
- **`make stop`**: Para o container em execução.
- **`make clean`**: Remove o container.

## Observações
- Certifique-se de que o Docker está instalado e em execução na sua máquina antes de usar os comandos acima.
- O arquivo `.env` deve ser configurado corretamente com as variáveis de ambiente necessárias para o funcionamento da aplicação.or e-mail
