from ChainingHashTableMap import ChainingHashTableMap
class Playlist():
    def __init__(self):
        self.music_map = ChainingHashTableMap()
        self.first_song = None
        self.last_song = None

    def add_song(self, new_song_name):
        if self.first_song is None and self.last_song is None:
            self.first_song = new_song_name
            self.last_song = new_song_name
        else:
            self.music_map[new_song_name] = None
            self.music_map[self.last_song] = new_song_name
            self.last_song = new_song_name

    def add_song_after(self, song_name, new_song_name):
        old_next = self.music_map[song_name]
        self.music_map[song_name] = new_song_name
        self.music_map[new_song_name] = old_next
        if old_next == None:
            self.last_song = new_song_name

    def play_song(self, song_name):
        print("Playing:", song_name)

    def play_list(self):
        curr_song = self.first_song
        while curr_song is not None:
            self.play_song(curr_song)
            curr_song = self.music_map[curr_song]