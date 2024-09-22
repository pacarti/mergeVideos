#!/usr/bin/python

# mergeVideos.py - creates a txt list of videos that the folder contains. After, it is passed to ffmpeg to merge them. 

import os, sys, re, subprocess
from pathlib import Path

def isFilenameValid(videoFileName):
    properFileNameRegex = re.compile(r'^[a-zA-Z0-9._-]+$') 
    # ^ and $ used so that entire string is matched from the beginning to the end.
    if properFileNameRegex.match(videoFileName):
        return True

def main():

    videosDir = Path(sys.argv[1])  

    if sys.argv[1] == '--help':
        print("Syntax: mergeVideos.sh path/to/video files")
        exit()
    os.chdir(videosDir)


    listFile = open('list.txt', 'w')

    mp4FilesCount = 0
    webmFilesCount = 0
    mkvFilesCount = 0


    for file in sorted(os.listdir(videosDir)):
        # print(file)
        if file.endswith('.mp4'):
            if isFilenameValid(file):
                # listFile.write('file ' + '\'' + file + '\'\n')
                mp4FilesCount += 1
                # print(file)
            else:
                print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.\nPlease rename the file: " + file + ".")
                exit()

        if file.endswith('.webm'):
            if isFilenameValid(file):
                # listFile.write('file ' + '\'' + file + '\'\n')
                webmFilesCount += 1
            else:
                print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.\nPlease rename the file: " + file + ".")
                exit()
        if file.endswith('.mkv'):
            if isFilenameValid(file):
                # listFile.write('file ' + '\'' + file + '\'\n')
                mkvFilesCount += 1
            else:
                print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.\nPlease rename the file: " + file + ".")
                # sys.exit(0)
                exit()
            
    if mp4FilesCount > 0 and webmFilesCount == 0 and mkvFilesCount == 0:
        # Only MP4 files.
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mp4'):
                listFile.write('file ' + '\'' + file + '\'\n')
        sys.exit(1)
    elif webmFilesCount > 0 and mp4FilesCount == 0 and mkvFilesCount == 0:
        # print("Only WEBM files.")
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.webm'):
                listFile.write('file ' + '\'' + file + '\'\n')
        sys.exit(2)
    elif mkvFilesCount > 0 and mp4FilesCount == 0 and webmFilesCount == 0:
        # Only MKV files.
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mkv'):
                listFile.write('file ' + '\'' + file + '\'\n')
        sys.exit(3)

    elif mp4FilesCount > webmFilesCount and mp4FilesCount > mkvFilesCount:
        # Majority MP4 files.
        # If the majority is MP4, convert the rest to mp4
        for file in os.listdir(videosDir):
                if file.endswith('.webm') or file.endswith('.mkv'):
                    subprocess.run([os.path.dirname(os.path.abspath(__file__)) + "/./convertToMp4.sh", file])
        # After the conversion, write the new converted filenames to list.txt
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mp4'):
                listFile.write('file ' + '\'' + file + '\'\n')
        # Do the concatenation of MP4 files
        sys.exit(1)

    elif webmFilesCount > mp4FilesCount and webmFilesCount > mkvFilesCount:
        # Majority WEBM files.
        # If the majority is WEBM, convert the rest to webm
        for file in os.listdir(videosDir):
                if file.endswith('.mp4') or file.endswith('.mkv'):
                    subprocess.run([os.path.dirname(os.path.abspath(__file__)) + "/./convertToWebm.sh", file])
        # After the conversion, write the new converted filenames to list.txt
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.webm'):
                listFile.write('file ' + '\'' + file + '\'\n')
        # Do the concatenation of WEBM files
        sys.exit(2)

    elif mkvFilesCount > webmFilesCount and mkvFilesCount > mp4FilesCount:
        # Majority MKV files.
        # If the majority is MKV, convert the rest to mkv
        for file in os.listdir(videosDir):
                if file.endswith('.mp4') or file.endswith('.webm'):
                    subprocess.run([os.path.dirname(os.path.abspath(__file__)) + "/./convertToMkv.sh", file])
        # After the conversion, write the new converted filenames to list.txt
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mkv'):
                listFile.write('file ' + '\'' + file + '\'\n')
        # Do the concatenation of MKV files
        sys.exit(3)

if __name__ == "__main__":
    main()

# After the proper list.txt file is created, the rest(ffmpeg command) is executed in the shell script.
