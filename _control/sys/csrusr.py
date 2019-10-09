# -*- coding: utf-8 -*-

from datedelta import datedelta, datetime
from dateutil.parser import parse


class CSRUSR:

    def __init__(self, 
                 matricula='', 
                 situacao=0,
                 nome='',
                 setor='',
                 funcao='',
                 senha='',
                 redefinir=False,
                 frequencia=0):
        self.matricula = str(matricula)
        self.situacao = int(situacao)
        self.nome = str(nome)
        self.setor = int(setor)
        self.funcao = str(funcao)
        self.senha = str(senha)
        if redefinir:
            self.redefinir = 1
        else:
            self.redefinir = 0
        self.frequencia = int(frequencia)