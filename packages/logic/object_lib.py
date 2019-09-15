# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:19:43 2018

"""

# from postgresql.entitydb import *
from models.entities import *
from packages.postgresql.repository import *
import socket
#from postgresql import entitydb, repository 

def CreatePreco1(nome, valor, data):
    preco1 = Precos1()
    preco1.nome = nome
    preco1.valor = valor
    preco1.data = data

def CreatePreco2(nome, valor, data):
    preco2 = Precos2()
    preco2.nome = nome
    preco2.valor = valor
    preco2.data = data