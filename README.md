# Kizuna Sports

Esse é um sistema de consulta de quadras e orçamento esportivo, desenvolvido
durante meu aprendizado de Python.

## Estado atual — v0.1.0

Permite:

- Consultar as quadras cadastradas.
- Selecionar uma quadra.
- Informar uma quantidade inteira de horas.
- Calcular o valor do orçamento.
- Tratar entradas que não representam números inteiros.
- Realizar várias consultas até escolher sair.

Os dados e preços são fictícios.

## Tecnologias utilizadas

- Python 

## Como executar

Com Python instalado, execute na pasta do projeto:

    python main.py

No Windows, também é possível utilizar:

    py main.py

## Limitações atuais

- Os dados das quadras estão definidos no código.
- O programa não consulta disponibilidade de horários.
- O orçamento não cria uma reserva.
- Não há banco de dados, autenticação ou pagamento.
 (É apenas uma breve demonstração de como vai ser o projeto.)

## Evolução planejada

- Cadastro e consulta de reservas.
- Persistência de dados.
- Backend com Django e PostgreSQL.
