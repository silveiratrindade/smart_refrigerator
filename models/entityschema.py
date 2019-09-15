from datetime import date
from marshmallow import Schema, fields, pprint


class Preco1Sch(Schema):
    nome_produto = fields.Str()
    valor = fields.Float()
    data = fields.Date()

class Preco2Sch(Schema):
    nome_produto = fields.Str()
    valor = fields.Float()
    data = fields.Date()
