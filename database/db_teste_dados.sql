/* Conecta ao banco de dados criado */

CONNECT 'C:\Users\ferna\Documents\Python Exemplos\Firebird\db_teste.fdb'  USER 'SYSDBA' PASSWORD 'masterkey';

/* Insere dados nas tabelas de pessoas */

INSERT INTO MRP$PESSOAS (nome_formal,nome_alternativo,end_logradouro,end_numero,end_bairro,end_municipio,end_estado,cad_federal,cad_estadual)
VALUES ('FERNANDO VICENTE BATISTA','VICENTE','RUA 47','452','SANTA TEREZA','GOIANÉSIA','GO','61648019153', '13098798-00');

INSERT INTO MRP$PESSOAS (nome_formal,nome_alternativo,end_logradouro,end_numero,end_bairro,end_municipio,end_estado)
VALUES ('POLIANE CUNHA DE SOUZA BATISTA','POLIANE','RUA 47','452','SANTA TEREZA','GOIANÉSIA','GO');

INSERT INTO MRP$TELEFONE_PESSOAS (id_pessoa,tipo,numero,contato)
VALUES (1,'CEL','(65)9-9925-1782','VICENTE');

INSERT INTO MRP$TELEFONE_PESSOAS (id_pessoa,tipo,numero,contato)
VALUES (2,'CEL','(65)9-9680-8875','POLIANE');

/* Grava dados */

COMMIT;

/* Insere dados nas tabelas de produtos */

INSERT INTO MRP$CLASSES (descricao)
VALUES ('COSMÉTICOS');

INSERT INTO MRP$CLASSES (descricao)
VALUES ('TECIDOS');

INSERT INTO MRP$CLASSES (descricao)
VALUES ('ENXOVAL');

INSERT INTO MRP$GRUPOS (descricao, id_classe)
VALUES ('HIGIENE PESSOAL', 1);

INSERT INTO MRP$GRUPOS (descricao, id_classe)
VALUES ('PLANOS', 2);

INSERT INTO MRP$GRUPOS (descricao, id_classe)
VALUES ('MALHAS', 2);

INSERT INTO MRP$GRUPOS (descricao, id_classe)
VALUES ('COLCHAS', 3);

INSERT INTO MRP$GRUPOS (descricao, id_classe)
VALUES ('LENÇÓIS', 3);

INSERT INTO MRP$SUBGRUPOS (descricao, id_grupo)
VALUES ('SHAMPOO', 1);

INSERT INTO MRP$SUBGRUPOS (descricao, id_grupo)
VALUES ('TAFETÁ', 2);

INSERT INTO MRP$SUBGRUPOS (descricao, id_grupo)
VALUES ('SARJA', 2);

INSERT INTO MRP$SUBGRUPOS (descricao, id_grupo)
VALUES ('MALHA DUPLA', 3);

INSERT INTO MRP$SUBGRUPOS (descricao, id_grupo)
VALUES ('CANELADA', 3);

INSERT INTO MRP$SUBGRUPOS (descricao, id_grupo)
VALUES ('COM ELÁSTICO', 5);

INSERT INTO MRP$SUBGRUPOS (descricao, id_grupo)
VALUES ('BABADO', 5);

INSERT INTO MRP$PRODUTOS (situacao, descricao_curta, descricao, embalagem, id_subgrupo)
VALUES (1, 'JLCS 30 CE', 'JOGO LENÇOL CASAL MALHA FIO 30.1 COM ELÁSTICO','3 PEÇAS', 6);

INSERT INTO MRP$PRODUTOS (situacao, descricao_curta, descricao, embalagem, id_subgrupo)
VALUES (1, 'JLKS 30 CE', 'JOGO LENÇOL KING SIZE MALHA FIO 30.1 COM ELÁSTICO','3 PEÇAS', 6);

INSERT INTO MRP$PRODUTOS (situacao, descricao_curta, descricao, descricao_completa, embalagem, id_subgrupo)
VALUES (1, 'MAL30P160', 'MALHA 30.1 PENTEADA 160 g/m2','Material:100% ALGODÃO; Largura:1,20m, Rendimento:2,60 m/kg; Gramatura: 160 g/m3','METRO', 6);

INSERT INTO MRP$PROD_MARCAS (nome_marca, modelo, id_produto)
VALUES ('FIO SUL','215',4);

COMMIT;

