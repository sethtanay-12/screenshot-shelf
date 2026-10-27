from pathlib import Path

def get_recent_screenshots(folder, n=10):
    folder = Path(folder)


    screen_shots = []
    for f in folder.iterdir():
        if f.is_file() == True: #takes only files not any folders or anything
            if f.suffix.lower() in {".jpg",".jpeg",".png"}: #checks for capital case file types
                screen_shots.append(f)
    print(len(screen_shots))

if __name__ == "__main__":
    get_recent_screenshots(r"C:\Users\T  A  N  A  Y\Pictures\Screenshots", 5)