# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:37:32 2018

@author: adm_silveiratrindade
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

class CreateSession:     
    
    def __new__(self, url_db = 'postgresql://postgres:postgres@localhost/mercado'):        
        ''' database_platform://database_user:password@hostname_or_ip/database_name'''

        self.string_con = url_db
        
        # an Engine, which the Session will use for connection resources
        self.db_engine = create_engine(self.string_con, poolclass=NullPool)
    
        # create a configured "Session" class
        self.Session = sessionmaker(bind=self.db_engine)   
        
        # create a Session
        self.sess = self.Session() 
        
        return self.sess       
