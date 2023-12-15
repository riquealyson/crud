CREATE DATABASE Amenic;
USE Amenic;

CREATE TABLE filmes (id INT PRIMARY KEY AUTO_INCREMENT,
    tituloFilme VARCHAR(200) NOT NULL,
    generoFilme VARCHAR(100) NOT NULL
);

INSERT INTO filmes (tituloFilme, generoFilme) 
VALUES ('The Lord of the Rings: The Fellowship of the Ring', 'Fantasy'),
    ('The Lord of the Rings: The Two Towers', 'Fantasy'),
    ('The Lord of the Rings: The Return of the King', 'Fantasy');


SELECT * FROM filmes;