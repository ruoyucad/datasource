import pandas as pd 
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_config import credential 

sp = spotipy.Spotify() 

cid = credential['clientID'] 
secret = credential['clientSecrect']
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 


BQB5wdUDAz5NCUu5WwEhBdprWGsAsiS_R9fVbgnRoczeqtf8FyrsSSzZDLi-wHC2u14otRXY1-FLQOGcGKcyllPNNX44kK7MecSM8SomvffOC93aqDjdB9xy_5Da6nWF_8CaiC7dELPOEOxcIWx-m0M-T99I5pJimqv37Du08px1MZ9LVs002t1ZNDUENxE3iA2aNu99_WIjRauGi9_Xp7lCTdTr8Ybmls3C08hPPrZj02EpkuHr3cU6ZD11tFaZ1BUzinqpt3c
sp.trace=False 

# playlist is chill vibes
myplaylist = sp.user_playlist('bossangelo','37i9dQZF1DX889U0CL85jj' )