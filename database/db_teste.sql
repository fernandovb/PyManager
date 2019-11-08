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

CREATE DATABASE 'E:\PyManager\database\contabil.fdb' USER 'FERNANDO' PASSWORD '123456'
	DEFAULT CHARACTER SET ISO8859_1 COLLATION PT_BR;

/* Conecta ao banco de dados criado */

CONNECT 'E:\PyManager\database\contabil.fdb'  USER 'SYSDBA' PASSWORD 'masterkey';
SET NAMES ISO8859_1;

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

/* Estrutura do NCM/SH - Nomenclatura Comum do Mercosul / Sistema Harmonizado
	11 22 33 4 5
	1 = Capítulo 2 primeiros dígitos do SH
	2 = Posição 4 primeiros dígitos do SH
	3 = Subposição 6 primeiros dígitos do SH
	4 = Item 7 dígito do NCM
	5 = Subitem 8 dígito do NCM*/

/* Tabela de Capítulos NCM/SH */
CREATE TABLE SEB$ERNCMCP (
	id_capitulo CHAR(2),
	descricao VARCHAR(300),
	CONSTRAINT SEB$PK_ERNCMCP PRIMARY KEY (id_capitulo)
);

/* Tabela de NCM/SH*/
CREATE TABLE SEB$ERNCM (
	id_ncm CHAR(8),
	id_capitulo INTEGER,
	descricao VARCHAR(500) NOT NULL,
	vigencia_ini DATE NOT NULL,
	vigencia_fim DATE,
	id_umd INTEGER,
	CONSTRAINT SEB$PK_ERNCM PRIMARY KEY (id_ncm),
	CONSTRAINT SEB$FK_ERNCM_ERNCMCP FOREIGN KEY (id_capitulo),
	CONSTRAINT SEB$FK_ERNCM_ERUMD FOREIGN KEY (id_umd)
);

/* Tabela de unidades de medida (UMD) */
CREATE TABLE SEB$ERUMD (
	id_umd INTEGER,
	descricao VARCHAR(100),
	abr_umd CHAR(5),
	CONSTRAINT SEB$PK_ERUMD PRIMARY KEY (id_umd),
	CONSTRAINT SEB$UK_ERUMD UNIQUE (abr_umd)
);

/* Tabela de CEST - Código Estruturado da Substituição Tributária */

CREATE TABLE SEB$ERCEST (
	id_cest CHAR(7),
	descricao VARCHAR(650),
	vigencia_ini DATE NOT NULL,
	vigencia_fim DATE,
	CONSTRAINT SEB$PK_ERCEST PRIMARY KEY (id_cest)
);

/* Tabela de relação NCM e CEST */

CREATE TABLE SEB$ERCTNC (
	id_cest CHAR(7),
	id_ncm CHAR(8)
);
