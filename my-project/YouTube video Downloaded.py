# pip install pytube
import pytube

link = input('Enter YouTube Video URL')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded', link)