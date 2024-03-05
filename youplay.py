from pytube import *
from moviepy.editor import *
import os

def download_playlist(playlist_url, output_folder):
    playlist = Playlist(playlist_url)

    for video_url in playlist.video_urls:
        video = YouTube(video_url)
        video_stream = video.streams.filter(only_audio=True).first()
        video_stream.download(output_folder)

        video_path = os.path.join(output_folder, video_stream.default_filename)
        mp3_path = os.path.splitext(video_path)[0] + ".mp3"
        video_clip = AudioFileClip(video_path)
        video_clip.write_audiofile(mp3_path)

        os.remove(video_path)

if __name__ == "__main__":
    playlist_url = input("INPUT THE PLAYLIST URL")
    output_folder = input("INPUT THE FILE PATH")
    download_playlist(playlist_url, output_folder)
