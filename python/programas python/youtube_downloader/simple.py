from pytube import Playlist
from pytube import YouTube

playlist = Playlist('https://www.youtube.com/playlist?list=PLyLfJxrkCuyBaCzUbUEmoAn4vDVhQ6HKn')
for video_url in playlist.video_urls:
    print(video_url)
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    file_name = yt.title
    print(file_name)
    stream.download()
#    converter(file_name)
