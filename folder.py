import logging
import os

from settings import *
from Shooter import Shooter


def scan_folder(folder):
    # print '**** processing:', folder
    logging.info('**** processing folder:{}'.format(folder))

    movie_files = [f for f in os.listdir(folder) if f.endswith('.mp4') or f.endswith('.mkv') or f.endswith('.avi')]

    for movie_file in movie_files:
        movie_file_full_path = os.path.join(folder, movie_file)

        # if subtitle already exist, ignore it
        srt_full_path = os.path.join(folder, movie_file + '.chn.srt')
        ass_full_path = os.path.join(folder, movie_file + '.chn.ass')
        sub_full_path = os.path.join(folder, movie_file + '.chn.sub')
        if os.path.exists(srt_full_path) or os.path.exists(ass_full_path) or os.path.exists(sub_full_path):
            # print '---- subtitle already get: {}'.format(movie_file)
            logging.info('---- EXIST subtitle for: {}'.format(movie_file))
            continue

        # print '++++ subtitle for movie file: {}'.format(movie_file)

        shooter = Shooter(movie_file_full_path)
        count = shooter.start()
        logging.info('----  GET {} subtitle for {}'.format(count, movie_file))
        # detail.append((movie_file_full_path, count))

    if settings[SETTING_RECURSIVE]:
        sub_folders = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
        for sub_folder in sub_folders:
            ignore_hidden = settings[SETTING_IGNORE_HIDDEN]
            if ignore_hidden:
                if sub_folder.startswith("."):
                    continue
            sub_folder_full_path = os.path.join(folder, sub_folder)
            scan_folder(sub_folder_full_path)

