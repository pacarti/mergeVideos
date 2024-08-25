#!/usr/bin/python

# mergeVideos.py - creates a txt list of videos that the folder contains. After, it is passed to ffmpeg to merge them. 


def isFilenameValid(videoFileName):
    properFileNameRegex = re.compile(r'^[a-zA-Z0-9._-]+$') 
    # ^ and $ used so that entire string is matched from the beginning to the end.
    if properFileNameRegex.match(videoFileName):
        return True

import os, sys, re
from pathlib import Path

# TODO: Step 2. Execute the proper command in ffmpeg and pass the file


videosDir = Path(sys.argv[1])

os.chdir(videosDir)


listFile = open('list.txt', 'w')

for folderName, subfolders, filenames in os.walk(videosDir):
    # Sort the filenames alphabetically:
    filenames.sort()
    for file in filenames:
        if file.endswith('.mp4') or file.endswith('.webm') or file.endswith('.mkv'):
            if isFilenameValid(file):
                listFile.write('file ' + '\'' + file + '\'\n')
                # print(file)
            else:
                print("The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'. Please rename the file: " + file + ".")
                exit()
