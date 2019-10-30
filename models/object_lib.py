# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:19:43 2018

"""

# from postgresql.entitydb import *
from models.entities import Precos1, Precos2
# from models.entityschema import Preco1Sch, Preco2Sch
# from packages.postgresql.repository import *
# import socket
#from postgresql import entitydb, repository 

def CreatePreco1(produto, valor, data):
    preco1 = Precos1()
    preco1.produto = produto
    preco1.valor = valor
    preco1.data = data
    return preco1

def CreatePreco2(produto, valor, data):
    preco2 = Precos2()
    preco2.produto = produto
    preco2.valor = valor
    preco2.data = data
    return preco2

