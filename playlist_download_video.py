from pytube import Playlist

link = 'https://www.youtube.com/playlist?list=PL47q1VKS2cizjqtCHynhMpLU8Ptc3xqxB'

plylst = Playlist(link)

print(f'Downloading: {plylst.title}')

# download audio
for video in plylst.videos:
    video.streams.filter(only_audio=True).first().download(r'G:\Desktop\New_plylst')