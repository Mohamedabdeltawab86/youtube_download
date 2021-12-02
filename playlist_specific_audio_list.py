from pytube import YouTube, Playlist


link = "https://www.youtube.com/watch?v=maUT-ez8DU0&list=PLMESC_UFcDHIFSQAWGvXNzEQW50ba3jfm&index="

playlist = Playlist(link)


for video in playlist[10:18]:
    v = YouTube(video)
    # download audio
    v.streams.filter(only_audio=True).first().download()
    
