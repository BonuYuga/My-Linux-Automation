import os
import shutil

folder = os.path.expanduser("~/Downloads")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Code": [".py", ".js", ".html", ".css"],
}

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()
        for category, extensions in categories.items():
            if ext in extensions:
                dest = os.path.join(folder, category)
                os.makedirs(dest, exist_ok=True)
                shutil.move(filepath, dest)
                print(f"Moved: {filename} → {category}")
                break