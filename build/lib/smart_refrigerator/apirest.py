from operator import and_, or_, not_
from sqlalchemy import desc
from datetime import datetime
# from models.entities import Eventdatum, Logicalsensor, NodeIntegratedboard, Node
# from packages.postgresql.repository import Repository
# from webservice.entityschema import EventDatumSchema, NodeSchema

from models.entityschema import Preco1Sch, Preco2Sch
from packages.postgresql.repository import *
import socket


# def GetData(repository, node_num, start_datetime=datetime.now(), end_datetime=datetime.now()):
#     """Get data from database with requests parameters, and return data in JSON format."""

#     if(end_datetime == ''):
#         end_datetime = datetime.now()

#     node = repository.GetFirst(Node, Node.name == 'NODE'+ str(node_num), Node.nodeid)
#     intboard = repository.GetFirst(NodeIntegratedboard, NodeIntegratedboard.nodeid == node.nodeid, NodeIntegratedboard.intboardid)
#     logsensor = repository.GetAll(Logicalsensor, Logicalsensor.intboardid == intboard.intboardid)
#     data = []
#     for sensor in logsensor:
#         eventlist = repository.GetAll(Eventdatum, and_(and_(Eventdatum.logicalsensorid == sensor.logicalsensorid, Eventdatum.timestampdata >= start_datetime), Eventdatum.timestampdata <= end_datetime))
#         if len(eventlist) != 0:
#             for event in eventlist:

#                 data.append(event)       

#     data.sort(key=lambda x:x.eventdataid, reverse=False)

#     schema = EventDatumSchema(many=True)
#     result = schema.dump(data)                

#     return result

# def GetNodes(repository):
#     # rep = Repository()

#     nodes = []
#     nodes = repository.GetAll(Node)
    
#     for n in nodes:
#         if(n.name == 'NODE0'):
#             nodes.remove(n)
    
#     schema = NodeSchema(many=True)
#     result = schema.dump(nodes)

#     return result
    
# def GetLastRegister(repository):    

#     nodes = []
#     intboard = []
#     logsensor = []
#     event = []

#     nodes = repository.GetAll(Node)
    
#     for n in nodes:
#         if(n.name == 'NODE0'):
#             nodes.remove(n)

#     for n in nodes:

#         intboard.append(repository.GetFirst(NodeIntegratedboard, NodeIntegratedboard.nodeid == n.nodeid, NodeIntegratedboard.intboardid))


#     for i in intboard:

#         logsensor.append(repository.GetAll(Logicalsensor, Logicalsensor.intboardid == i.intboardid))

#     for l in logsensor:
#         for e in l:

#             event.append(repository.GetFirst(Eventdatum, Eventdatum.logicalsensorid == e.logicalsensorid, Eventdatum.timestampdata))

#     schema = EventDatumSchema(many=True)
#     result = schema.dump(event)  

#     return result




def GetPreco1(repository):
    # rep = Repository()

    preco1 = []
    preco1 = repository.GetAll(Precos1)
    
    
    schema = Preco1Sch(many=True)
    result = schema.dump(preco1)

    return result


def main():



    pass

if __name__ == '__main__':
    main()