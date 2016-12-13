from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Content(Base):
	__tablename__ = 'content'
	
	title = Column(String(), primary_key=True)
	content = Column(String())
	time = Column(Integer())

engine = create_engine('mysql+mysqlconnector://root:@10.9.155.162:3306/blog')
DBSession = sessionmaker(bind=engine)
