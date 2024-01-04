#Importing random for generating random ratings 
import random
#Class Audio 
class Audio:
    def __init__(self, url, name):#Passing URL and name along with random ratings 
        self.url = url
        self.name = name
        self.ratings = []

    def add_rating(self, rating):#Function for add ratings
        self.ratings.append(rating)

    def get_average_rating(self):#Function for average ratings
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings) #Calculating the average rating sum of rating devided by total number of ratings
#Playlist class 
class Playlist:
    def __init__(self, name, genre): #Initialising name and genre along with audio file and ratings
        self.name = name
        self.genre = genre
        self.audio_files = []
        self.ratings = []

    def add_audio(self, audio):#Function to add audio
        self.audio_files.append(audio)

    def add_rating(self, rating):#ratings 
        self.ratings.append(rating)

    def get_average_rating(self):#Average ratings 
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

#User class 
class User:
    def __init__(self, name):#initialising user name 
        self.name = name
#Audio Mnager class 
class AudioManager:
    def __init__(self):#initialising user , audio file and playlists
        self.users = []
        self.audios = []
        self.playlists = []

    def create_user(self, name):#Function to create the user list
        user = User(name)
        self.users.append(user)#appending user name 
        return user

    def create_audio(self, url, name):#Function to create a audio file 
        audio = Audio(url, name)
        self.audios.append(audio)#appending Audio
        return audio

    def create_playlist(self, name, genre):#Function to create a playlist
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)#appending playlist
        return playlist

    def add_audio_to_playlist(self, playlist, audio):#Function to add audio to a playlist
        playlist.add_audio(audio)

    def add_rating_to_audio(self, audio, rating):#Function to add ratings to audio
        audio.add_rating(rating)

    def add_rating_to_playlist(self, playlist, rating):#Function to add ratings to playlist
        playlist.add_rating(rating)

    def search_audio_by_name(self, name):#Function to search an audio by name 
        return [audio for audio in self.audios if audio.name.lower() == name.lower()]

    def search_playlist_by_name(self, name):#Function to search a playlist by name 
        return [playlist for playlist in self.playlists if playlist.name.lower() == name.lower()]

def generate_random_ratings():#Function to generate a random ratings 
    return random.randint(1, 5)

def display_average_ratings(audio_manager):#Function to display the average ratings based on random ratings 
    for audio in audio_manager.audios:
        print(f"Average rating for {audio.name}: {audio.get_average_rating()}")

    for playlist in audio_manager.playlists:
        print(f"Average rating for {playlist.name}: {playlist.get_average_rating()}")

if __name__ == "__main__":
    audio_manager = AudioManager()

    for i in range(1, 4):
        user_name = input(f"Enter name for User {i}: ")
        audio_manager.create_user(user_name)

    audio_name = input("Enter audio name: ")
    audio_url = input("Enter audio URL: ")
    audio = audio_manager.create_audio(audio_url, audio_name)

    playlist_name = input("Enter playlist name: ")
    playlist_genre = input("Enter playlist genre: ")
    playlist = audio_manager.create_playlist(playlist_name, playlist_genre)

    audio_manager.add_audio_to_playlist(playlist, audio)

    for i in range(3):
        random_rating = generate_random_ratings()
        audio_manager.add_rating_to_audio(audio, random_rating)
        audio_manager.add_rating_to_playlist(playlist, random_rating)

    display_average_ratings(audio_manager)
