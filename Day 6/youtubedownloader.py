import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from PIL import ImageTk
import pytube
import pytube.helpers

window = ttk.Window(themename='darkly')
window.title('YouTube downloader')
window.geometry('1100x200')
#directory_icon = ImageTk.PhotoImage(file=r'C:\Users\UZ1\Desktop\daily-coding\daily-coding\Day 6\directory.png')
directory_path = tk.StringVar()
youtube_url = tk.StringVar()


def get_path():
    path_file = filedialog.askdirectory()
    directory_path.set(path_file)

def convert():
    path_file = directory_path.get()
    yt_url = youtube_url.get()
    pytube.helpers.target_directory(path_file)
    yt = pytube.YouTube(yt_url)
    yt.streams.get_audio_only().download(path_file)




title_label = ttk.Label(window, text='YouTube downloader by Jonathan', font=('Calibri 10 bold'))
url_label = ttk.Label(window, text='Enter url from YouTube: ', font=('Calibra 16'))
url_entry =  ttk.Entry(window, width='100', textvariable=youtube_url)
path_button = ttk.Button(window, text='Path button', command=get_path)
path_label = ttk.Label(window, text='Enter path where file will be download:', font=('Calibra 16'))
path_url_entry = ttk.Entry(window, width='100', textvariable=directory_path)
action_button = ttk.Button(window, text='Click to convert', command=convert)

title_label.grid(row=0, column=0)
url_label.grid(row=1, column=0, padx=10)
url_entry.grid(row=1, column=1)
path_label.grid(row=2, column=0, padx=10)
path_url_entry.grid(row=2, column=1, pady=30)
path_button.grid(row=2, column=2, padx=10)
action_button.grid(row=3, column=1)

# link = str(input('Insert link: '))
# path = str(input(r'Insert where: '))

window.mainloop()