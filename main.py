import sys
import os

from pip._vendor.distlib.compat import raw_input


def batch_rename(directory, show_name, season, extension):
    for count, filename in enumerate(os.listdir(os.chdir(fr"{directory}"))):
        count += 1
        count = str(count)
        dst = show_name + " - " + season + "x" + count.zfill(2) + extension
        src = directory + filename
        dst = directory + dst
        print(src)
        print(dst)
        os.rename(src, dst)


if __name__ == '__main__':
    directory = raw_input("Paste directory: ")

    print("Enter Show Name: ")
    show_name = str(input())

    print("Enter season number: ")
    season = str(input())

    extension = raw_input("Enter extension(.mkv, .mp4, etc): ")

    batch_rename(directory, show_name, season, extension)
