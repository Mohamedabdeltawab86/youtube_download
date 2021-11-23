from pytube import YouTube, Playlist

link = 'https://youtube.com/playlist?list=PL914QhoC1Bhu0qe8DeK7HXYl9KD1GaZ5d'

plylst = Playlist(link)

print(f'Downloading: {plylst.title}')

for video in plylst.videos:
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(r'G:\Desktop\New_plylst')
