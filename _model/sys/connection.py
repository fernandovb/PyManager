# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Connection(object):
    Base = declarative_base()

    def __engine__(self, user, pw, host, db):
        self.user = user
        self.pw = pw
        self.host = host
        self.db = db
        try:
            engine = create_engine(f'firebird+fdb://{self.user}:{self.pw}@{self.host}/{self.db}', 
                                        pool_size=10, 
                                        max_overflow=20, 
                                        convert_unicode=True)
            self.Session = sessionmaker(bind=engine)
            self.connection = engine.connect()
            mensagem = f'Conectado em "{self.host}:{self.db}"'
            status = True
        except exc.DatabaseError as error:
            mensagem = f'Dados para conexão incorretos. \nErro: {error}'
            status = False
        except:
            mensagem = 'Erro ao realizar a conexão! '
            status = False
        finally:
            return [status, mensagem]
    
    def close_connection(self):
        self.connection.close()
