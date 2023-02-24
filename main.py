import youtube_dl
# import server
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Rachel, Eryn, and Meg"}

@app.get("/download_audio/{youtube_url:path}") # optional user path to download into
# @app.route("/download_audio/{youtube_url:path}", name="path-convertor")
async def download_audio(youtube_url: str):
    # download_audio(youtube_url)
    # msg.body = {url: 'youtube.com/23513'}
    return {"message": f"Downloading YouTube video {youtube_url}"}

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
    # download_audio(yt_url)


# # main()
# if __name__ == "__main__":
#     server.run()


