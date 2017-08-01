import sqlalchemy
import sqlalchemy.orm
from data.modelbase import SqlAlchemyBase


class Track(SqlAlchemyBase):
      __tablename__ = 'Track'
      id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
      name = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
      length = sqlalchemy.Column(sqlalchemy.Integer)
      audio_url = sqlalchemy.Column(sqlalchemy.String)
      video_url = sqlalchemy.Column(sqlalchemy.String)
      display_order = sqlalchemy.Column(sqlalchemy.Integer, index=True)

      album_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Album.id'))
                                          # Name of the table and back_populates = field
      album = sqlalchemy.orm.relationship('Album', back_populates='tracks')