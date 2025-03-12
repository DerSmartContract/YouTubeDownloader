import yt_dlp


def download_video(url, output_path="downloads"):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",  # Falls Audio/Video getrennt sind, wird MP4 erstellt
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "noplaylist": True,  # Falls es Teil einer Playlist ist, nur das eine Video laden
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=qnXfZ_cQgEU"
    download_video(video_url)
