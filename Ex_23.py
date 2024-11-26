import requests 
class Music:
    def __init__(self, name, singer, album, link):
        self.name = name
        self.singer = singer
        self.album = album
        self.link = link

    def __str__(self):
        return f"Track Name: {self.name}, Artist: {self.singer}, Album: {self.album}, iTunes_Link: {self.link}" 
    
class SongFetcher:
    def __init__(self, url):
        self.url = url 

    def search_track(self, track_name):
        respond = requests.get(self.url) 
        data = respond.json() 
        