#!/usr/bin/python

# mergeVideos.py - creates a txt list of videos that the folder contains. After, it is passed to ffmpeg to merge them. 

# The name cannot contain spacebar or non-English signs. Therefore - create a Regex that would check if the name is proper. If not, then it would return an information about that.

# def checkNameValidity

import os, sys
from pathlib import Path

# TODO: Step 2. Execute the proper command in ffmpeg and pass the file


videosDir = Path(sys.argv[1])

os.chdir(videosDir)


listFile = open('list.txt', 'w')

for folderName, subfolders, filenames in os.walk(videosDir):
    # Sort the filenames alphabetically:
    filenames.sort()
    for file in filenames:
        # for char in file:
            # print(char)
        # filenames.sort(reverse=True)
        if file.endswith('.mp4') or file.endswith('.webm') or file.endswith('.mkv'):
            listFile.write('file ' + '\'' + file + '\'\n')
            # print(file)
