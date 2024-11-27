import requests 
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

    @staticmethod 
    def read_data(song):
        name = song["trackName"] 
        artist = song["artistName"] 
        album = song.get("collectionName", "No Album")
        link = song.get("trackViewUrl", "No Link")
        return name, artist, album, link 

    def search_track(self, name): 
        respond = requests.get(self.url) 
        data = respond.json() 
        track_data = data["results"] 
        tracks = [] 
        for song in track_data:
            if name == song["trackName"]:
                name, artist, album, link = self.read_data(song) 
                music_obj = Music(name, artist, album, link) 
                tracks.append(music_obj)
                return tracks 
            else:
                print(f"{name} Not Found!") 

if __name__ == "__main__":
    track_name = input("Enter track name for search: ") 
    url = f"https://itunes.apple.com/search?term={track_name}&media=music" 
    obj = SongFetcher(url) 
    obj.search_track(track_name)  