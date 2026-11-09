CREATE DATABASE IF NOT EXISTS kizuna_sports;
USE kizuna_sports;

CREATE TABLE quadras (
    nome TEXT,
    modalidade TEXT,
    preco_por_hora INTEGER,
    coberta INTEGER,
    capacidade_jogadores INTEGER
);


INSERT INTO quadras (nome, modalidade, preco_por_hora, coberta, capacidade_jogadores)
VALUES
    ('Society 01', 'Society', 100, 1, 67),
    ('Areia 01', 'Areia', 70, 0, 50);
    
    SELECT nome,preco_por_hora FROM quadras
    WHERE preco_por_hora <=80;
    
    SELECT USER(), VERSION();