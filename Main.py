#!/usr/bin/env python
import os
import sys

import argparse
import logging
import time

from folder import scan_folder
from settings import *


def init_logging():
    logging_dir = 'logging'
    if not os.path.exists(logging_dir):
        os.makedirs(logging_dir)

    logging.basicConfig(filename='{}/shooter_{}.log'.format(logging_dir, time.strftime('%m%d%H%M')), level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console)


if __name__ == '__main__':
    print("Welcome to ShooterSubPyDownloader")

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source_folder", help="the folder(s) to scan. (use delimiter to specify multi folder)")
    parser.add_argument("-r", "--recursive", help="scan recursively, y or n")
    parser.add_argument("-i", "--ignore_hidden", help="ignore hidden file, y or n")
    args = parser.parse_args()

    source_folder = args.source_folder
    recursive = args.recursive
    if not recursive:
        settings[SETTING_RECURSIVE] = DEFAULT_SETTING_RECURSIVE
    else:
        settings[SETTING_RECURSIVE] = recursive.lower() == 'y'
    ignore_hidden = args.ignore_hidden
    if not ignore_hidden:
        settings[SETTING_IGNORE_HIDDEN] = DEFAULT_SETTING_IGNORE_HIDDEN
    else:
        settings[SETTING_IGNORE_HIDDEN] = ignore_hidden.lower() == 'y'

    if not source_folder:
        print 'source folder must be provided'
        sys.exit()

    movie_dirs = source_folder.split(',')

    init_logging()

    for movie_dir in movie_dirs:
        scan_folder(movie_dir)
        # print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        # for entry in detail:
        #     print '{} : {}'.format(entry[1], entry[0])
        # print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
