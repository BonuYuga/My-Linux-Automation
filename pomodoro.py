import time
import os

def countdown(minutes, label):
    seconds = minutes * 60
    print(f"\n{label} dimulai! ({minutes} menit)")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r{timer}", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    print("\nSelesai!")
    os.system('notify-send "Pomodoro" "Waktu habis!"')

def pomodoro():
    sesi = 1
    while True:
        print(f"\n=== SESI {sesi} ===")
        countdown(25, "Fokus kerja")
        
        if sesi % 4 == 0:
            countdown(15, "Istirahat panjang")
        else:
            countdown(5, "Istirahat pendek")
        
        sesi += 1
        input("\nTekan Enter untuk mulai sesi berikutnya...")

pomodoro()