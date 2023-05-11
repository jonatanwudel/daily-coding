import tkinter as tk
import ttkbootstrap as ttk
import pytube
import pytube.helpers

link = str(input('Insert link: '))
path = str(input(r'Insert where: '))
#pytube.helpers.target_directory('C:\Users\UZ1\Desktop\daily-coding\daily-coding\Day 6')
yt = pytube.YouTube(link)
yt.streams.get_audio_only().download(path)