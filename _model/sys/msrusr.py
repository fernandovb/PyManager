# -*- coding: utf-8 -*-

import _model.sys.global_conn as gconn
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, SMALLINT
from sqlalchemy.orm import relationship
from _model.sys.msrstr import MSRSTR


class MSRUSR(gconn.conn.Base):
    __tablename__ = 'SYS$SRUSR'

    id_matricula = Column(VARCHAR(32), primary_key=True)
    situacao = Column(SMALLINT)
    nome_usuario = Column(VARCHAR(50))
    id_setor = Column(Integer)
    id_funcao = Column(Integer)
    senha = Column(VARCHAR(30))
    redefinir = Column(VARCHAR(30))
    frequencia = Column(Integer)

    #MSRSTR.setor = relationship('SYS$SRSTR', order_by=id_setor, back_populates='ID_SETOR')

    def __init__(self, id_matricula, 
                       situacao=0, 
                       nome_usuario='', 
                       id_setor=0, 
                       id_funcao=0, 
                       senha='', 
                       redefinir=0, 
                       frequencia=0):
        self.id_matricula = id_matricula
        self.situacao = situacao
        self.nome_usuario = nome_usuario
        self.id_setor = id_setor
        self.id_funcao = id_funcao
        self.senha = senha
        self.redefinir = redefinir
        self.frequencia = frequencia

    def __repr__(self):
        return f'{self.id_matricula}-{self.nome_usuario}'

    def find_user(self, user):
        session = gconn.conn.Session()
        consulta = session.query(MSRUSR).filter_by(id_matricula=user).first()
        return consulta
