import os
import subprocess

def download_video_youtube_dl(url: str, save_path: str):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        command = [
            "yt-dlp",
            url,
            "-o", os.path.join(save_path, "%(title)s.%(ext)s"),  
            "--format", "best[ext=mp4]"
        ]

        subprocess.run(command, check=True)
        print(f"Видео успешно скачано в: {save_path}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при скачивании: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")