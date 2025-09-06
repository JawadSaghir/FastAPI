from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker

DataBase_Url= "sqlite:///MyDataBase.db"
engine= create_engine(DataBase_Url, echo= True, connect_args={"check_same_thread": False})

SessionLocal= sessionmaker(bind= engine, autocommit= False, autoflush= False)

Base= declarative_base()

conn= engine.connect()
records= conn.execute(text('SELECT * FROM Blogs'))

conn.commit()
print(records)