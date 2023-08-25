import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("My Music Player")
music_player.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='yellow', selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

current_song_index = 0  # Initialize the index of the current playing song

def play():
    global current_song_index  # Use the global variable to update the index
    current_song_index = play_list.curselection()[0]
    pygame.mixer.music.load(os.path.join(directory, play_list.get(current_song_index)))
    var.set(play_list.get(current_song_index))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def next_song():
    global current_song_index  # Use the global variable to update the index
    current_song_index = (current_song_index + 1) % play_list.size()
    play_list.selection_clear(0, tkr.END)
    play_list.activate(current_song_index)
    play_list.selection_set(current_song_index)
    play()

def prev_song():
    global current_song_index  # Use the global variable to update the index
    current_song_index = (current_song_index - 1) % play_list.size()
    play_list.selection_clear(0, tkr.END)
    play_list.activate(current_song_index)
    play_list.selection_set(current_song_index)
    play()

Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")
Button5 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="NEXT", command=next_song, bg="green", fg="white")
Button6 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PREV", command=prev_song, bg="maroon", fg="white")

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
Button5.pack(fill="x")
Button6.pack(fill="x")
play_list.pack(fill="both", expand="yes")

# Play the first song in the list when the program starts
if song_list:
    play_list.selection_set(0)
    play()

music_player.mainloop()
