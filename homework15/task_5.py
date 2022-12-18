from peewee import *

db = SqliteDatabase('chinook.db')


class BaseModel(Model):
    class Meta:
        database = db


class Albums(BaseModel):
    title = CharField(column_name='Title', null=False)
    album_id = AutoField(column_name='Albumid')

    class Meta:
        table_name = 'albums'


class Tracks(BaseModel):
    name = CharField(column_name='Name', null=False)
    album_id = AutoField(column_name='Albumid')

    class Meta:
        table_name = 'tracks'


def get_tracks():
    album_name = input('Введите название альбома: ')  
    with db:
        return Tracks.select().\
            where(Tracks.album_id == Albums.select().where(Albums.title == album_name))

tracks = get_tracks()
for track in tracks:
    print(track.name)

