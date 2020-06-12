from pytube import YouTube
from pytube import Playlist
import os
from tkinter import *


#ffmpeg -i Sambinha.mp4 Sambinha.mp3



def video_download(video_url):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    file_name = yt.title
    print(file_name)
    stream.download()
    converter(file_name)

def playlist_download(video_url):
    playlist = Playlist(video_url)
    for video_url in playlist.video_urls:
        print(video_url)
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        file_name = yt.title
        print(file_name)
        stream.download()
        converter(file_name)


def converter(file_name):
    try:
        os.rename(file_name+'.webm',file_name+'.mp3')
    except:
        os.rename(file_name+'.mp4',file_name+'.mp3')

#programa principal em loop
while True:
    print('digite sair para sair')
    video_url = (input('url='))
    if video_url == 'sair':
        break
    else:
        video_download(video_url)

