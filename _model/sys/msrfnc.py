# -*- coding: utf-8 -*-

import _model.sys.global_conn as gconn
from sqlalchemy import Column, Integer, VARCHAR

class MSRFNC():
    __tablename__ = 'SYS$SRFNC'

    id_funcao = Column(Integer, primary_key=True)
    nome_funcao = Column(VARCHAR(30))

    def __repr__(self):
        return f'{self.id_funcao}-{self.nome_funcao}'