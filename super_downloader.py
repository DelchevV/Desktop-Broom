import os, pytube
from moviepy.editor import *

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folder_path = os.path.join(desktop_path,"Music")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def download_audio_from_youtube(link):
    try:
        yt = pytube.YouTube(link)  # Update here
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = os.path.join(folder_path, f"{yt.title}.mp3")
        audio_stream.download(output_path=folder_path)

        # Convert the downloaded audio to MP3 format
        video_clip = VideoFileClip(audio_file_path)
        video_clip.audio.write_audiofile(audio_file_path)
        video_clip.close()
        print(f"Downloaded: {yt.title} as MP3")
    except pytube.exceptions.VideoUnavailable:
        print(f"Error: Video {link} is unavailable")
    except Exception as e:
        print(f"Error during downloading {link}: {e}")

def download_audio_from_file(file_path):
    with open(file_path, 'r') as f:
        links = f.readlines()

        for link in links:
            link.strip()
            if link:
                download_audio_from_youtube(link)


music_txt_path= os.path.join(desktop_path, 'music.txt')
download_audio_from_file(music_txt_path)

