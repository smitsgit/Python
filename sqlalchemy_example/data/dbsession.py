import sqlalchemy
import sqlalchemy.orm

from data.modelbase import SqlAlchemyBase

# if we dont do this thing , Python doesnt know that these classes
# are deriving from SqlAlchemyBase required on #19 cause its all runtime and no compile time
import data.album
import data.track


class DbSessionFactory():
    factory = None

    @staticmethod
    def global_init_database(db_file):

        if DbSessionFactory.factory:
            return

        if not db_file:
            raise Exception('You must specify the DB file')

        conn_str = 'sqlite:///' + db_file
        engine = sqlalchemy.create_engine(conn_str, echo=True)

        # I will look for all the classes who derive from me and then load them in DB
        SqlAlchemyBase.metadata.create_all(engine)

        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)

        # session = DbSessionFactory.factory()

    @staticmethod
    def create_session():
        return DbSessionFactory.factory()
