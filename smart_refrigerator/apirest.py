from operator import and_, or_, not_
from sqlalchemy import desc
from datetime import datetime
from models.entities import Precos1, Precos2
from models.entityschema import Preco1Sch, Preco2Sch
from packages.postgresql.repository import *
import socket


def GetPreco1(repository):
    # rep = Repository()

    preco1 = []
    preco1 = repository.GetAll(Precos1)    
    
    schema = Preco1Sch(many=True)
    result = schema.dump(preco1)

    return result
    
def GetItemByID(repository, id):

    item = repository.Get(Precos1, id)
    schema = Preco1Sch()
    result = schema.dump(item)

    return result

def GetItemByProduto(repository, predicate):

    item = repository.GetFirst(Precos1, predicate, Precos1.produto)
    schema = Preco1Sch()
    result = schema.dump(item)

    return result

def main():

    rep = Repository()

    item = rep.GetFirst(Precos1, Precos1.produto=='ovos', Precos1.produto)

    print(item.produto)


    pass

if __name__ == '__main__':
    main()