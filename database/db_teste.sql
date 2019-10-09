/* Base de dados criada utilizado padrão Firbird/IBExpert*/
/* Padronização de prefixos
	id_  : representa uma chave primária
	end_ : representa as partes que compõem o endereço
	nome_: representa as nomeações da entidade
  */
  
 /* Grupos de tabelas
	SYS$ : (System) tabelas de controle do sistema.
	SEB$ : (Parameter) tabelas de parâmetros do sistema;
	PRM$ : (People Relamationship Manager) tabelas para uso de relacionamento de pessoas;
	ACC$ : (Account) tabelas para uso na contabilidade;
	FMI$ : (Financial) tabelas para uso no controle financeiro;
	CLC$ : (Contracts) tabelas para uso no controle de contratos;
	TAX$ : (Taxes) tabelas para uso da área fiscal;
	MRP$ : (M) tabelas para uso de controle de produtos e estoques;
 */

CREATE DATABASE 'E:\PyManager\database\contabil.fdb' USER 'SYSDBA' PASSWORD 'masterkey';

/* Conecta ao banco de dados criado */

CONNECT 'E:\PyManager\database\contabil.fdb'  USER 'SYSDBA' PASSWORD 'masterkey';

/* Cria domínios */

CREATE DOMAIN SYS$DON_TIPO_TELEFONE AS CHAR(3) DEFAULT 'COM' CHECK (VALUE IN ('COM', 'RES', 'CEL'));
CREATE DOMAIN SYS$DON_SITUACAO AS SMALLINT DEFAULT 0 CHECK (VALUE IN (0,1,2,3,9));
CREATE DOMAIN SYS$DON_BOOL AS SMALLINT DEFAULT 0 CHECK (VALUE IN (0,1));

/* Tabela de Setores */
CREATE TABLE SYS$SRSTR (
	id_setor INTEGER,
	nome_setor VARCHAR(30),
	CONSTRAINT SYS$SRSTR PRIMARY KEY (id_setor)
);

/* Tabela de Funções */
CREATE TABLE SYS$SRFNC (
	id_funcao INTEGER,
	nome_funcao VARCHAR(30),
	CONSTRAINT SYS$SRFNC PRIMARY KEY (id_funcao)
);

/* Tabela de Usuários */
CREATE TABLE SYS$SRUSR (
	id_matricula VARCHAR(32),
	situacao SYS$DON_SITUACAO,
	nome_usuario VARCHAR(50),
	id_setor INTEGER,
	id_funcao INTEGER,
	senha VARCHAR(30),
	redefinir SYS$DON_BOOL,
	frequencia INTEGER,
	CONSTRAINT SYS$PK_SRUSR PRIMARY KEY (id_matricula),
	CONSTRAINT SYS$FK_SRSTR_SRUSR FOREIGN KEY (id_setor) REFERENCES SYS$SRSTR,
	CONSTRAINT SYS$FK_SRFNC_SRUSR FOREIGN KEY (id_funcao) REFERENCES SYS$SRFNC
);
