from models.entities import *
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.pool import NullPool


def main():

    database_name = 'mercado'
    engine = create_engine('postgresql://postgres:postgres@localhost/' + database_name, poolclass=NullPool)

    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()