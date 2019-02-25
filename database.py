from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name,like):
    cat_object = Cat(name=name,like = like)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats
def add_like(id):
	to_like = session.query(Cat).filter_by(id=id).first()
	to_like.like = to_like.like+1
	