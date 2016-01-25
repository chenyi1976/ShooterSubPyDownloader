#!/usr/bin/env python
import os
import sys

from folder import scan_folder

if __name__ == '__main__':
    print("Welcome to ShooterSubPyDownloader")

    movie_dirs = [os.curdir]
    if len(sys.argv) >= 2:
        movie_dirs = sys.argv[1:]

    for movie_dir in movie_dirs:
        scan_folder(movie_dir)
