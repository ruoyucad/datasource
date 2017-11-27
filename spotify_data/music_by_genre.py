import pandas as pd 
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_config import credential 
from sqlalchemy import create_engine  
import pymysql
import aquire_music
#Hiphop, pop,country ,dance,r&b
"" = ['Pop','Country','RNB']
playListID = ['37i9dQZF1DWXT8uSSn6PRy','37i9dQZF1DWSK8os4XIQBk','37i9dQZF1DX2WkIBRaChxW']
username = 'Spotify'
datalist= []
print('here we go')


pop = aquire_music.getData(username,'37i9dQZF1DWXT8uSSn6PRy')
Country = aquire_music.getData(username,'37i9dQZF1DWSK8os4XIQBk')
RNB = aquire_music.getData(username,'37i9dQZF1DX2WkIBRaChxW')
workout = aquire_music.getData(username,'37i9dQZF1DX76Wlfdnj7AP') 

#making database connection
myconnection = create_engine('mysql+pymysql://angelo:!Qry778899@127.0.0.1/angelo?charset=utf8')
print('db connected ...')
print('writing data to database now... ')
# creating table 'mymusic'
pd.io.sql.to_sql(pop,"Pop", myconnection, schema='angelo', if_exists='append')  
pd.io.sql.to_sql(Country,"Country", myconnection, schema='angelo', if_exists='append') 
pd.io.sql.to_sql(RNB,"RNB", myconnection, schema='angelo', if_exists='append') 
pd.io.sql.to_sql(workout,"Workout", myconnection, schema='angelo', if_exists='append') 
print('Complete !')