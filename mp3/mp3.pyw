import pygame
import tkinter as ttk
from tkinter.filedialog import askdirectory
import os

musicplayer = ttk.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = ttk.Listbox(musicplayer, bg = "light blue", selectmode = ttk.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(ttk.ACTIVE))
    var.set(playlist.get(ttk.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = ttk.Button(musicplayer,bg = "red",width=5,height=3,text = "PLAY",command = play)
Button2 = ttk.Button(musicplayer,bg = "blue",width=5,height=3,text = "STOP",command = ExitMusicPlayer)
Button3 = ttk.Button(musicplayer,bg= "green",width=5,height=3,text = "PAUSE",command = pause)
Button4 = ttk.Button(musicplayer,bg = "purple",width=5,height=3,text = "UNPAUSE",command = unpause)

var = ttk.StringVar()
songtitle = ttk.Label(musicplayer,textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()
