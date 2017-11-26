import pandas as pd 
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_config import credential 
from sqlalchemy import create_engine  
import pymysql

# get authorized by spotify
sp = spotipy.Spotify() 
cid = credential['clientID'] 
secret = credential['clientSecrect']
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
sp.trace=False 

# playlist contains 83 songs
myplaylist = sp.user_playlist('bossangelo','5StZ5Iuq3puwrJKsg2Sdh0' )
songs = myplaylist['tracks']['items']
ids = []
for i in range(len(songs)):
    ids.append(songs[i]['track']['id'])
    
songNames = []
for i in range(len(songs)):
    songNames.append(songs[i]['track']['name'])

# adding song attributes
features = sp.audio_features(ids)
musicdata = pd.DataFrame(features)
musicdata['song_name'] = songNames
musicdata['song_ids'] = ids
print('Done !')

#making database connection
myconnection = create_engine('mysql+pymysql://angelo:!Qry778899@127.0.0.1/angelo?charset=utf8')
print('db connected ...')
print('writing data to database now... ')
pd.io.sql.to_sql(musicdata,'mymusic', myconnection, schema='angelo', if_exists='append')  
print('Complete !')