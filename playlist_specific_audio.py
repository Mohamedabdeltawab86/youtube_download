from pytube import YouTube, Playlist


link = 'https://www.youtube.com/playlist?list=PLMESC_UFcDHIFSQAWGvXNzEQW50ba3jfm'

plylst = Playlist(link)

# print(f'Downloading: {plylst.title}')

# download audio
for video in plylst.videos:
    if 12 in str(video.title):
        with open('a.txt', 'w', encoding='utf-8-sig') as f:
            f.write(str(video.title))
            # video.streams.filter(only_audio=True).first().download(f)
            # print(video.title, f)
    else:
        print("Not Downloading your video")
        # video.streams.filter(only_audio=True).first().download(r'G:\Desktop\New_plylst\باقي الترمذي')
        

