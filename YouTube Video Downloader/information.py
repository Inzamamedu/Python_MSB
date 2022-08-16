from pytube import YouTube
path = "D:/Python_MSB/YouTube Video Downloader/download video"

url =  input("Enter URL: ")
try:
    yt = YouTube(url)
except ConnectionError:
    print("Connection Error")

print(yt.title)
print(yt.length)
print(yt.views)
print(yt.description)