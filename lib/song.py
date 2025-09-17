class Song:
    count = 0
    genre_count = {}
    artist_count = {}

    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
            Song.genres.append(genre) 
        Song.genre_count[genre] += 1

        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
            Song.artists.append(artist) 
        Song.artist_count[artist] += 1

    