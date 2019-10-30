from datetime import date
from marshmallow import Schema, fields, pprint


class Preco1Sch(Schema):
    id = fields.Int()
    produto = fields.Str()
    valor = fields.Float()
    data = fields.Date()

class Preco2Sch(Schema):
    id = fields.Int()
    produto = fields.Str()
    valor = fields.Float()
    data = fields.Date()
