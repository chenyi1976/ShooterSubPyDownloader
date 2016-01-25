import os
from Shooter import Shooter


def scan_folder(folder):
    print '**** processing:', folder

    movie_files = [f for f in os.listdir(folder) if f.endswith('.mp4') or f.endswith('.mkv') or f.endswith('.avi')]

    for movie_file in movie_files:
        print '++++ subtitle for movie file: {}'.format(movie_file)
        movie_file_full_path = os.path.join(folder, movie_file)
        shooter = Shooter(movie_file_full_path)
        shooter.start()

    sub_folders = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
    for sub_folder in sub_folders:
        sub_folder_full_path = os.path.join(folder, sub_folder)
        scan_folder(sub_folder_full_path)
