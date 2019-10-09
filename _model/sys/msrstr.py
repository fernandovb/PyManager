# -*- coding: utf-8 -*-

import _model.sys.global_conn as gconn
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class MSRSTR(gconn.conn.Base):
    __tablename__ = 'SYS$SRSTR'

    id_setor = Column(Integer, primary_key=True)
    nome_setor = Column(VARCHAR(30))

    def __repr__(self):
        return f'{self.id_setor}-{self.nome_setor}'