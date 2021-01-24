import sys
import os
import tkinter as tk
from tkinter import simpledialog
from pip._vendor.distlib.compat import raw_input


def batch_rename(path, show, season):
    extension = ""
    extensions = [".mkv", ".mp4"]
    for count, filename in enumerate(os.listdir(os.chdir(fr"{path}"))):
        if filename.endswith(tuple(extensions)):
            if filename.endswith(".mkv"):
                extension = ".mkv"
            elif filename.endswith(".mp4"):
                extension = ".mp4"
            count += 1
            count = str(count)
            dst = show + " - " + season + "x" + count.zfill(2) + extension
            src = path + filename
            dst = path + dst
            os.rename(src, dst)


if __name__ == '__main__':
    """
    master = tk.Tk()
    master.withdraw()

    directory = simpledialog.askstring(title="Directory", prompt="Enter the directory")
    show_name = simpledialog.askstring(title="Show Name", prompt="Enter the show name")
    season_number = simpledialog.askstring(title="Season", prompt="Enter the season number")
    extension = simpledialog.askstring(title="Extension", prompt="Enter the extension")
    """

    # ask for our directory as raw input because a string will mess up the input we give
    directory = raw_input("Paste directory: ")

    # ask for our show name as a string as it most likely will not have anything weird in it
    print("Enter Show Name: ")
    show_name = str(input())

    # ask for our season number as a string because it should just be a single number
    print("Enter season number(1, 2, 3, etc): ")
    season_number = str(input())

    # ask for our extension as raw input as we will have a period in it which might cause problems
    # extension = raw_input("Enter extension(.mkv, .mp4, etc): ")

    batch_rename(directory, show_name, season_number)
