import os

from sqlalchemy.orm import joinedload

from data.dbsession import DbSessionFactory
from data.album import Album
from data.track import Track

tracks = [
    {'duration': '0:48', 'title': 'Welcome to the millennium'},
    {'duration': '4:20', 'title': 'Renegade coders'},
    {'duration': '5:01', 'title': 'Cyberpunks unite!'},
    {'duration': '3:21', 'title': "We're all moving the Silicon Valley"},
    {'duration': '2:22', 'title': "Tomorrow's people"},
    {'duration': '4:24', 'title': 'I thought you were a robot'}
]


def init_db():
    top_dir = os.path.dirname(__file__)
    rel_path = os.path.join('db', 'database.sqlite')
    db_file = os.path.join(top_dir, rel_path)
    print(db_file)
    DbSessionFactory.global_init_database(db_file)


def insert_some_data():
    session = DbSessionFactory.create_session()
    album = Album()
    album.id = 1
    album.is_published = True
    album.name = 'Uptown'
    album.price = 56.10
    album.album_image = 'http://cat.img'

    for order, item in enumerate(tracks):
        track = Track()
        track.name = item['title']
        track.length = item['duration']
        track.display_order = order
        album.tracks.append(track)
    session.add(album)
    session.commit()


def retrieve_some_data():
    session = DbSessionFactory.create_session()

    # this causes only single query using joins because of .options(joinedload("tracks"))

    album = session.query(Album) \
        .options(joinedload("tracks"))\
        .filter(Album.id == 1) \
        .one()

    # album_two_queries = session.query(Album) \
    #     .filter(Album.id == 1) \
    #     .one()

    for track in album.tracks:
        print(track.name)


def update_some_data():
    session = DbSessionFactory.create_session()
    album = session.query(Album) \
        .options(joinedload("tracks")) \
        .filter(Album.id == 1) \
        .one()
    album.name = 'Uptown-modified'
    session.commit()
    pass


def delete_some_data():
    session = DbSessionFactory.create_session()
    album = session.query(Album) \
        .options(joinedload("tracks")) \
        .filter(Album.id == 1) \
        .one()
    session.delete(album)
    session.commit()
    pass


def main():
    init_db()
    # insert_some_data()
    retrieve_some_data()
    update_some_data()
    delete_some_data()


if __name__ == '__main__':
    main()
