import requests  # type: ignore
class Music:
    def __init__(self, name, singer, album, link):
        self.name = name
        self.singer = singer
        self.album = album
        self.link = link

    def __str__(self):
        return f"Track Name: {self.name}, \nArtist: {self.singer}, \nAlbum: {self.album}, \niTunes_Link: {self.link}" 
    
class SongFetcher:
    def __init__(self, url):
        self.url = url 

    def search_track(self):
        respond = requests.get(self.url) 
        data = respond.json() 
        print(data) 

if __name__ == "__main__":
    url = "https://itunes.apple.com/search?term={track_name}&media=music" 
    obj = SongFetcher(url) 
    obj.search_track() 