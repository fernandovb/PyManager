/* Conecta ao banco de dados criado */

CONNECT 'E:\PyManager\database\contabil.fdb'  USER 'SYSDBA' PASSWORD 'masterkey';

/* Insere dados em Setores */

INSERT INTO SYS$SRSTR (ID_SETOR, NOME_SETOR) 
VALUES (1, 'ADMINISTRAÇÃO');

INSERT INTO SYS$SRSTR (id_setor, nome_setor)
VALUES (2, 'TI');

INSERT INTO SYS$SRSTR (id_setor, nome_setor)
VALUES (3, 'CONTABILIDADE');

/* Insere dados em Funções */

INSERT INTO SYS$SRFNC (id_funcao, nome_funcao)
VALUES (1, 'GERENTE');

INSERT INTO SYS$SRFNC (id_funcao, nome_funcao)
VALUES (2, 'ADMINISTRADOR BD');

INSERT INTO SYS$SRFNC (id_funcao, nome_funcao)
VALUES (3, 'CONTABILISTA');

/* Insere dados de Usuários */

INSERT INTO SYS$SRUSR (id_matricula, situacao, nome_usuario, id_setor, id_funcao, senha, redefinir, frequencia)
VALUES ('FERNANDO', 0, 'FERNANDO VICENTE BATISTA', 3, 3, '123456', 0, 0);


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

