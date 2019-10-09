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
    id_setor = Column(Integer, ForeignKey('SYS$SRSTR.ID_SETOR'))
    id_funcao = Column(Integer)
    senha = Column(VARCHAR(30))
    redefinir = Column(VARCHAR(30))
    frequencia = Column(Integer)

    MSRSTR.setor = relationship('SYS$SRSTR', order_by=id_setor, back_populates='ID_SETOR')

    def __repr__(self):
        return f'{self.id_matricula}-{self.nome_usuario}'
