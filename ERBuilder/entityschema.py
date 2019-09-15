from datetime import date
from marshmallow import Schema, fields, pprint


class Preco1(Schema):
    nome = fields.Str()
    valor = fields.Float()
    data = fields.DateTime()

class Preco2(Schema):
    nome = fields.Str()
    valor = fields.Float()
    data = fields.DateTime()
