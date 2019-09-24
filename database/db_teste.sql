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

/* Cria domínio */

CREATE DOMAIN SEB$DON_TIPO_TELEFONE AS CHAR(3) DEFAULT 'COM' CHECK (VALUE IN ('COM', 'RES', 'CEL'));
CREATE DOMAIN SEB$DON_SITUACAO AS SMALLINT DEFAULT 0 CHECK (VALUE IN (1,2,3,9));

/* Cria tabelas do sistema para cadastro de acessos, codificações, parâmetros gerais etc. */

CREATE TABLE SYS$SETORES (
	id_setor SMALLINT,
	nome_setor VARCHAR(30),
);

CREATE TABLE SYS$USUARIOS (
	id_usuario VARCHAR(32),
	nome_usuario VARCHAR(50),
	funcao VARCHAR(30),
	setor VARCHAR(30),
	CONSTRAINT SYS$PK_USUARIO PRIMARY KEY (id_usuario)
);
