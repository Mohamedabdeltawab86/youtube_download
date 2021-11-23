from pytube import YouTube


# function to download video
def download_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first()
    stream.download(path)

# function to download audio
def download_audio(url, path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(path)



url = input("Enter the url of the video: ")
path = input("Enter the path to save the video: ")

video_type = input("Enter the type of video to download (video/audio): ")
if video_type == "video":
    download_video(url, path)
elif video_type == "audio":
    download_audio(url, path)
else:
    print("Invalid input")
    exit()

