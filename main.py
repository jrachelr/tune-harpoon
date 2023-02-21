import youtube_dl


def download_audio(yt_url):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])


def main():
    yt_url = "https://www.youtube.com/watch?v=8OAPLk20epo"
    download_audio(yt_url)


main()
