from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link)

yt.streams.get_highest_resolution().download("**Your Repository**")