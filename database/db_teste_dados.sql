/* Conecta ao banco de dados criado */

CONNECT 'E:\PyManager\database\contabil.fdb'  USER 'SYSDBA' PASSWORD 'masterkey';
SET NAMES ISO8859_1;

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
VALUES ('SYSDBA', 0, 'SYSDBA USUÁRIO MASTER', 2, 2, 'masterkey', 0, 0);

/* Grava dados */

COMMIT;

/* Insere dados nas tabelas de produtos */
