# coding: utf-8
from sqlalchemy import Column, Date, Float, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Precos1(Base):
    __tablename__ = 'precos1'

    id = Column(Integer, primary_key=True, server_default=text("nextval('precos1_preco_id_seq'::regclass)"))
    produto = Column(String(64), nullable=False)
    valor = Column(Float(53))
    data = Column(Date, nullable=False)


class Precos2(Base):
    __tablename__ = 'precos2'

    id = Column(Integer, primary_key=True, server_default=text("nextval('precos2_preco_id_seq'::regclass)"))
    produto = Column(String(64), nullable=False)
    valor = Column(Float(53))
    data = Column(Date, nullable=False)
