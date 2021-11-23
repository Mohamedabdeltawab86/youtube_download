from pytube import Playlist

link = 'https://www.youtube.com/watch?v=M3EHISMqWDI&list=PLMESC_UFcDHLrl1M1PGZ7SqR5w0100Qvq'

plylst = Playlist(link)

print(f'Downloading: {plylst.title}')

# download audio
for video in plylst.videos:
    video.streams.filter(only_audio=True).first().download(r'G:\Desktop\New_plylst')