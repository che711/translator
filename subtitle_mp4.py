import subprocess
import os
import re

def extract_subtitles_from_mp4(mp4_file, output_dir="."):
    # Получить информацию о треках
    cmd_probe = [
        "ffprobe", "-v", "error",
        "-select_streams", "s",
        "-show_entries", "stream=index:stream_tags=language",
        "-of", "default=noprint_wrappers=1:nokey=0",
        mp4_file
    ]
    
    result = subprocess.run(cmd_probe, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0 or not result.stdout:
        print("Субтитры не найдены или ошибка ffprobe.")
        print(result.stderr)
        return

    # Разбор ffprobe вывода
    streams = re.findall(r"index=(\d+).*?(?:language=([a-z]{2}))?", result.stdout, re.DOTALL)

    if not streams:
        print("Субтитровые треки не найдены.")
        return

    # Извлечение каждого субтитрового потока
    for i, (stream_index, lang) in enumerate(streams):
        lang = lang or "und"
        output_path = os.path.join(output_dir, f"subtitle_{i}_{lang}.srt")
        cmd_extract = [
            "ffmpeg", "-y", "-i", mp4_file,
            "-map", f"0:s:{i}", output_path
        ]
        print(f"Извлечение субтитров в {output_path}")
        subprocess.run(cmd_extract)

# Пример использования
extract_subtitles_from_mp4("../../Desktop/Плохие парни.2022.WEB-DL.2160p.DV.mp4", output_dir="subtitles")

