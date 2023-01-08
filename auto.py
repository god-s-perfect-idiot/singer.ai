from wonderwords import RandomWord 
from generator import gen_song, gen_title

r = RandomWord()
word = r.word()

def generate_song_lyrics():
    song = gen_song(word)
    title = gen_title(song)
    print(title+song)

# def generate_music():

if (__name__=='__main__'):
    generate_music()