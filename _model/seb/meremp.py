# -*- coding: utf-8 -*-

import _model.sys.global_conn as gconn
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, SMALLINT
from sqlalchemy.orm import relationship


class MEREMP(gconn.conn.Base):
    __tablename__ = 'SEB$EREMP'

    id_empresa = Column(Integer, primary_key=True)
