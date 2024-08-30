#!/usr/bin/python

# mergeVideos.py - creates a txt list of videos that the folder contains. After, it is passed to ffmpeg to merge them. 


def isFilenameValid(videoFileName):
    properFileNameRegex = re.compile(r'^[a-zA-Z0-9._-]+$') 
    # ^ and $ used so that entire string is matched from the beginning to the end.
    if properFileNameRegex.match(videoFileName):
        return True

import os, sys, re
from pathlib import Path


videosDir = Path(sys.argv[1])

os.chdir(videosDir)


listFile = open('list.txt', 'w')

mp4FilesCount = 0
webmFilesCount = 0
mkvFilesCount = 0

# for folderName, subfolders, filenames in os.walk(videosDir):
    # Sort the filenames alphabetically:
# filenames.sort()
for file in os.listdir(videosDir):
    if file.endswith('.mp4'):
        if isFilenameValid(file):
            listFile.write('file ' + '\'' + file + '\'\n')
            mp4FilesCount += 1
            # print(file)
        else:
            print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.\nPlease rename the file: " + file + ".")
            exit()

    elif file.endswith('.webm'):
        if isFilenameValid(file):
            listFile.write('file ' + '\'' + file + '\'\n')
            webmFilesCount += 1
        else:
            print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.\nPlease rename the file: " + file + ".")
            exit()
    elif file.endswith('.mkv'):
        if isFilenameValid(file):
            listFile.write('file ' + '\'' + file + '\'\n')
            mkvFilesCount += 1
        else:
            print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.\nPlease rename the file: " + file + ".")
            exit()
        
if mp4FilesCount > 0 and webmFilesCount == 0 and mkvFilesCount == 0:
    print("Only MP4 files.")
elif webmFilesCount > 0 and mp4FilesCount == 0 and mkvFilesCount == 0:
    print("Only WEBM files.")
elif mkvFilesCount > 0 and mp4FilesCount == 0 and webmFilesCount == 0:
    print("Only MKV files.")


# After the proper list.txt file is created, the rest(ffmpeg command) is executed in the shell script.