import sqlalchemy.ext.declarative as dec

# dec.declarative_base() in fact creates the class and hece S is caps in SqlAlchemyBase
# this is the class from which our model classes extend
SqlAlchemyBase = dec.declarative_base()
