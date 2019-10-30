""" Cornice services.
"""
from models.entityschema import Preco1Sch, Preco2Sch
from models.object_lib import *
from packages.postgresql.repository import Repository
from cornice import Service


hello = Service(name='hello', path='/', description="Simplest app")
preco1 = Service(name='preco1', path='/preco1')


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

@preco1.get()
def get_preco1(request):
    """Returns Hello in JSON."""

    rep = Repository()
    query = GetPreco1(rep)
    rep.Save()

    return query

@id.get()
def get_preco1(request):
    """Returns Hello in JSON."""

    id = int(request.GET.get('id',''))

    rep = Repository()
    query = GetPreco1(rep)
    rep.Save()

    return query

