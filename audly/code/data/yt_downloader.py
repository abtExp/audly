from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=5BDj0ow5hnA')

yt.streams\
    .filter(progressive=True, file_extension='mp4')\
    .order_by('resolution')\
    .desc()\
    .first()\
    .download()