import requests
import sys
import json
import urllib

spotifyURL = 'https://api.spotify.com/v1/'

# txt = 'reproduce |tive razão |track'
def execSpotify(txt):
    if "nextmusic" in txt:
        r = requests.post(spotifyURL+"me/player/next", headers= {'Accept': 'application/json' , 'Content-Type': 'application/json','Authorization':token})
        print(r.text)
        return "Tocando próxima música"
    elif "prevmusic" in txt:
        r = requests.post(spotifyURL+"me/player/previous", headers= {'Accept': 'application/json' , 'Content-Type': 'application/json','Authorization':token})
        print(r.text)
        return "Tocando música anterior"
    elif "volume" in txt:
        r = requests.put(spotifyURL+"me/player/volume?volume_percent="+txt.split("|")[1], headers= {'Accept': 'application/json' , 'Content-Type': 'application/json','Authorization':token})
        print(r.text)
    elif "reproduce" in txt:
        r = requests.get(spotifyURL+"search?limit=1&q="+txt.split("|")[1]+"&type="+txt.split("|")[2], headers= {'Accept': 'application/json' , 'Content-Type': 'application/json','Authorization':token})
        j = json.loads(r.text)
        print(r.text+"\n")
        dataa = {"context_uri": j['tracks']['items'][0]["album"]['uri'] ,"offset": {"position": j['tracks']['items'][0]['track_number']-1 },"position_ms": 0}
        dataa = json.dumps(dataa)
        r = requests.put(spotifyURL+"me/player/play", headers= {'Accept': 'application/json' , 'Content-Type': 'application/json','Authorization':token}, data = dataa)
        print("Reproduzindo:"+j['tracks']['items'][0]["album"]['uri']+" Track: "+str(j['tracks']['items'][0]['track_number'])+"\n:",dataa,r)

    # https://api.spotify.com/v1/search
