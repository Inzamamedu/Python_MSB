from pytube import YouTube
path = "D:/Python_MSB/YouTube Video Downloader/download video"

nods = int(input("Enter the number of download songs: "))
i = 1
while i <= nods:
    url =  input("Enter URL: ")
    try:
        yt = YouTube(url)
    except ConnectionError:
        print("Connection Error")
    download_video = yt.streams.get_by_resolution("720p")
    try:
        download_video.download(path)
    except AttributeError:
        print("Attribute Error")
    i += 1

print("Download Complete!")