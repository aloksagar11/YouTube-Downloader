# YouTube-Downloader
from pytube import YouTube
link = input("Paste Your Link Here : ")
youtube_1 = YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Enter Index for Download video : "))
print("Wait... Downloading.........")
videos[strm].download()
print("Successfully Downloaded")
