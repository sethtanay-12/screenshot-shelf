from pathlib import Path
from PIL import Image

def get_modified_time(f):
    return f.stat().st_mtime

def get_recent_screenshots(folder, n=10): #n =  defined so that if the user didnt pass any parameter so it has a default value to work with
    folder = Path(folder)


    screen_shots = []
    for f in folder.iterdir():
        if f.is_file() == True: #takes only files not any folders or anything
            if f.suffix.lower() in {".jpg",".jpeg",".png"}: #checks for capital case file types
                screen_shots.append(f)

    screen_shots = sorted(screen_shots , key = get_modified_time , reverse=True)

    screen_shots = screen_shots[:n] #sliced

    return screen_shots


def make_thumbnail(source , thumb_folder , size = (200,200)):
    source = Path(source)
    thumb_folder = Path(thumb_folder)

    thumb_folder.mkdir(exist_ok=True)
    thumb_path = thumb_folder / source.name

    return thumb_path

    

if __name__ == "__main__":
    shots = get_recent_screenshots(r"C:\Users\T  A  N  A  Y\Pictures\Screenshots", 5)
    path = make_thumbnail(shots[0], r"D:\Projects\screenshot-shelf\.thumbs")
    print(path)