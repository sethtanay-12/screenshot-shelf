from pathlib import Path

def get_modified_time(f):
    return f.stat().st_mtime

def get_recent_screenshots(folder, n=10):
    folder = Path(folder)


    screen_shots = []
    for f in folder.iterdir():
        if f.is_file() == True: #takes only files not any folders or anything
            if f.suffix.lower() in {".jpg",".jpeg",".png"}: #checks for capital case file types
                screen_shots.append(f)

    screen_shots = sorted(screen_shots , key = get_modified_time , reverse=True)

    screen_shots = screen_shots[:n] #sliced

    return screen_shots

if __name__ == "__main__":
    shots = get_recent_screenshots(r"C:\Users\T  A  N  A  Y\Pictures\Screenshots", 5)
    for s in shots:
        print(s.name)