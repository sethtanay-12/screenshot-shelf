import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap
from app import get_recent_screenshots, make_thumbnail

SCREENSHOT_FOLDER = r"C:\Users\T  A  N  A  Y\Pictures\Screenshots"
THUMB_FOLDER = r"D:\Projects\screenshot-shelf\.thumbs"

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Screen Shots")

    shots = get_recent_screenshots(SCREENSHOT_FOLDER, 5)   # a list with 5 items

    layout = QHBoxLayout()                                 # ONE row, made BEFORE the loop

    for s in shots:
        thumbnail = make_thumbnail(s, THUMB_FOLDER)        # small copy, returns its path
        pixmap = QPixmap(str(thumbnail))                   # load the small picture
        label = QLabel()                                   # an empty label
        label.setPixmap(pixmap)                            # put the picture into the label
        layout.addWidget(label)                            # hang it in the row, EVERY round

    window.setLayout(layout)                               # give the finished row to the window

    window.show()                                          # show only after everything is built
    sys.exit(app.exec())

if __name__ == "__main__":
    main()