# -*- coding: utf-8 -*-

import _model.sys.global_conn as gconn
from datedelta import datedelta, datetime
from dateutil.parser import parse
from _model.sys.msrusr import MSRUSR

class Error(Exception):
    
    def __init__(self, mensagem, funcao):
        self.mensagem = mensagem
        self.funcao = funcao

    def __str__(self):
        return f'Erro: {self.mensagem}; funcao: {self.funcao}'


class CSRUSR:

    def __init__(self, 
                 id_matricula='', 
                 situacao=0,
                 nome_usuario='',
                 id_setor=0,
                 id_funcao=0,
                 senha='',
                 redefinir=False,
                 frequencia=0):
        self.id_matricula = str(id_matricula).upper()
        self.situacao = int(situacao)
        self.nome_usuario = str(nome_usuario).upper()
        self.id_setor = int(id_setor)
        self.id_funcao = int(id_funcao)
        self.senha = str(senha)
        if redefinir:
            self.redefinir = 1
        else:
            self.redefinir = 0
        self.frequencia = int(frequencia)

    def ac_insert(self):
        session = gconn.conn.Session()
        usuario = MSRUSR(id_matricula=self.id_matricula, 
                         situacao=self.situacao,
                         nome_usuario=self.nome_usuario,
                         id_setor=self.id_setor,
                         id_funcao=self.id_funcao,
                         senha=self.senha,
                         redefinir=self.redefinir,
                         frequencia=self.frequencia)
        session.add(usuario)
        session.commit()
        session.close()
    
    def ac_update(self):
        session = gconn.conn.Session()
        usuario = session.query(MSRUSR).filter_by(id_matricula=self.id_matricula).one()
        usuario.situacao = self.situacao
        usuario.nome_usuario = self.nome_usuario
        usuario.id_setor = self.id_setor
        usuario.id_funcao = self.id_funcao
        usuario.senha = self.senha
        usuario.redefinir = self.redefinir
        usuario.frequencia = self.frequencia
        session.add(usuario)
        session.commit()
        session.close()
    
    def search_records(self):
        session = gconn.conn.Session()
        try:
            consulta = session.query(MSRUSR).filter_by(id_matricula=self.id_matricula).first()
            if consulta.id_matricula is None:
                raise Error('Registro não localizado', 'search_records(CSRUSR)')
            self.situacao = int(consulta.situacao)
            self.nome_usuario = str(consulta.nome_usuario)
            self.id_setor = int(consulta.id_setor)
            self.id_funcao = int(consulta.id_funcao)
            self.senha = str(consulta.senha)
            if consulta.redefinir == 1:
                self.redefinir = True
            else:
                self.redefinir = False
            self.frequencia = int(consulta.frequencia)
        finally:
            session.close()
    
    def search_all_records(self):
        session = gconn.conn.Session()
        consulta = session.query(MSRUSR).all()
        session.close()
        return consulta
