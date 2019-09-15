# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 19:28:49 2018

"""

from packages.postgresql.dbsession import CreateSession
# from models.entities import *
from sqlalchemy import and_, or_, not_

class Repository:
    
    def __init__(self):
        self.session = CreateSession()

    def Add(self, entity):
        
        self.session.add(entity)         

    def AddAll(self, entityList):
        
        self.session.add_all(entityList)    

    def Get(self, entity, ID):
              
        return self.session.query(entity).get(ID)       

    def GetFirst(self, entity, predicate, orderbydesc):
        ''' The predicate argument is optional. If you inform this, and after the returned list 
        will be filter by specific entity property criteria, only the first item would be selected.'''

        return self.session.query(entity).filter(predicate).order_by(orderbydesc.desc()).first()     
       
    def GetAll(self, entity, predicate = ''):
        ''' The predicate argument is optional. If you inform this, the returned list will be filter 
        by specific entity property criteria.
        Declair multiple filter as parameters, using the methods and_(), or_(), not_() as operators, inside predicate.'''
              
        return self.session.query(entity).filter(predicate).all()            
    
    def Remove(self, entity):
                
        self.session.delete(entity)
        
    def Save(self):    

        try:
            self.session.commit() 
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close_all()
                
        
        
        
