#!/usr/bin/python

# mergeVideos.py - creates a txt list of videos that the folder contains. After, it is passed to ffmpeg to merge them. 

import os, sys
from pathlib import Path

# TODO: Step 1. Create a txt file with 'file + 'video_file.mp4'' lines
# TODO: Step 2. Execute the proper command in ffmpeg and pass the file

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# os.chdir('/home/anon/Videos')

videosDir = Path(sys.argv[1])

os.chdir(videosDir)

# print(sys.argv[1])

# listFilename = videosDir

listFile = open('list.txt', 'w')

for folderName, subfolders, filenames in os.walk(videosDir):
    # Sort the filenames alphabetically:
    filenames.sort()
    for file in filenames:
        # filenames.sort(reverse=True)
        if file.endswith('.mp4') or file.endswith('.webm') or file.endswith('.mkv'):
            listFile.write('file ' + '\'' + file + '\'\n')
            # print(file)
