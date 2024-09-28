#!/usr/bin/python

# mergeVideos.py - creates a txt list of videos that the folder contains. After, it is passed to ffmpeg to merge them. 

# TODO: Add removing of the renamed files at the end

import os, sys, re, subprocess, shutil
from pathlib import Path

def isFilenameValid(videoFileName):
    properFileNameRegex = re.compile(r'^[a-zA-Z0-9._-]+$') 
    # ^ and $ used so that entire string is matched from the beginning to the end.
    if properFileNameRegex.match(videoFileName):
        return True

def main():

    videosDir = Path(sys.argv[1])  

    # videosDir = '/home/anon/Videos/mp4Files/'


    if sys.argv[1] == '':
        # If the user didn't specify the path, the message is sent in the Bash script, thus here exiting
        exit()

    elif sys.argv[1] == '--help':
        print("Syntax: mergeVideos.sh path/to/video files")
        exit()


    os.chdir(videosDir)


    listFile = open('list.txt', 'w')

    mp4FilesCount = 0
    webmFilesCount = 0
    mkvFilesCount = 0
    mp3FilesCount = 0


    newFiles = []


    for index, file in enumerate(sorted(os.listdir(videosDir))):
        if file.endswith('.mp4'):
            if isFilenameValid(file):
                mp4FilesCount += 1
            else:
                print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.")
                print("Incorrect filename of " + file + ". Copy and rename the file automatically?(It can affect the desired order, the new file will be deleted after merging.)[N/y]:", end='')
                renameChoice = input()
                if renameChoice == 'N' or renameChoice == 'n':
                    print("Please rename the file: " + file + " manually.")
                    exit()
                elif renameChoice == 'y' or renameChoice == 'Y':
                    if index < 10:
                        newFile = '0' + str(index) + '.mp4'
                    else:
                        newFile = str(index) + '.mp4'
                    shutil.copy(file, newFile)
                    newFiles.append(newFile)
                    mp4FilesCount += 1

        if file.endswith('.webm'):
            if isFilenameValid(file):
                webmFilesCount += 1
            else:
                print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.")
                print("Incorrect filename of " + file + ". Copy and rename the file automatically?(It can affect the desired order, the new file will be deleted after merging.)[N/y]:", end='')
                renameChoice = input()
                if renameChoice == 'N' or renameChoice == 'n':
                    print("Please rename the file: " + file + " manually.")
                    exit()
                elif renameChoice == 'y' or renameChoice == 'Y':
                    if index < 10:
                        newFile = '0' + str(index) + '.webm'
                    else:
                        newFile = str(index) + '.webm'
                    shutil.copy(file, newFile)
                    newFiles.append(newFile)
                    webmFilesCount += 1

        if file.endswith('.mkv'):
            if isFilenameValid(file):
                mkvFilesCount += 1
            else:
                print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.")
                print("Incorrect filename of " + file + ". Copy and rename the file automatically?(It can affect the desired order, the new file will be deleted after merging.)[N/y]:", end='')
                renameChoice = input()
                if renameChoice == 'N' or renameChoice == 'n':
                    print("Please rename the file: " + file + " manually.")
                    exit()
                elif renameChoice == 'y' or renameChoice == 'Y':
                    if index < 10:
                        newFile = '0' + str(index) + '.mkv'
                    else:
                        newFile = str(index) + '.mkv'
                    shutil.copy(file, newFile)
                    newFiles.append(newFile)
                    mkvFilesCount += 1

        elif file.endswith('.mp3'):
            if isFilenameValid(file):
                mp3FilesCount += 1
            else:
                print("The script applies only to video files in formats: .mp4, .webm. and .mkv. The video file name can contain only A-Z, a-z, 0-9, '.', '-' or '_'.")
                print("Incorrect filename of " + file + ". Copy and rename the file automatically?(It can affect the desired order, the new file will be deleted after merging.)[N/y]:", end='')
                renameChoice = input()
                if renameChoice == 'N' or renameChoice == 'n':
                    print("Please rename the file: " + file + " manually.")
                    exit()
                elif renameChoice == 'y' or renameChoice == 'Y':
                    if index < 10:
                        newFile = '0' + str(index) + '.mp3'
                    else:
                        newFile = str(index) + '.mp3'
                    shutil.copy(file, newFile)
                    newFiles.append(newFile)
                    mp3FilesCount += 1
    if mp4FilesCount > 0 and webmFilesCount == 0 and mkvFilesCount == 0 and mp3FilesCount == 0:
        # Only MP4 files.
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mp4') and isFilenameValid(file):
                listFile.write('file ' + '\'' + file + '\'\n')
        listFile.close()
        subprocess.run('ffmpeg -y -f concat -i list.txt -c copy output.mp4', shell=True, encoding='utf-8')
    elif webmFilesCount > 0 and mp4FilesCount == 0 and mkvFilesCount == 0 and mp3FilesCount == 0:
        # print("Only WEBM files.")
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.webm') and isFilenameValid(file):
                listFile.write('file ' + '\'' + file + '\'\n')
        subprocess.run('ffmpeg -y -f concat -i list.txt -c copy output.webm', shell=True, encoding='utf-8')
    elif mkvFilesCount > 0 and mp4FilesCount == 0 and webmFilesCount == 0 and mp3FilesCount == 0:
        # Only MKV files.
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mkv') and isFilenameValid(file):
                listFile.write('file ' + '\'' + file + '\'\n')
        subprocess.run('ffmpeg -y -f concat -i list.txt -c copy output.mkv', shell=True, encoding='utf-8')
    elif mp3FilesCount > 0 and mp4FilesCount == 0 and webmFilesCount == 0 and mkvFilesCount == 0:
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mp3') and isFilenameValid(file):
                listFile.write('file ' + '\'' + file + '\'\n')
        listFile.close()
        subprocess.run('ffmpeg -y -f concat -i list.txt -c copy output.mp3', shell=True, encoding='utf-8')

    elif mp4FilesCount > webmFilesCount and mp4FilesCount > mkvFilesCount:
        # Majority MP4 files.
        # If the majority is MP4, convert the rest to mp4
        for file in os.listdir(videosDir):
                if file.endswith('.webm') or file.endswith('.mkv'):
                    pfile = Path(file)
                    subprocess.run(f'ffmpeg -i {file} -c:v libx264 -crf 15 -c:a aac {pfile.stem}.mp4', shell=True, encoding='utf-8')
        # After the conversion, write the new converted filenames to list.txt
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mp4'):
                listFile.write('file ' + '\'' + file + '\'\n')
        # Do the concatenation of MP4 files
        listFile.close()
        subprocess.run('ffmpeg -y -f concat -i list.txt -c copy output.mp4', shell=True, encoding='utf-8')

    elif webmFilesCount > mp4FilesCount and webmFilesCount > mkvFilesCount:
        # Majority WEBM files.
        # If the majority is WEBM, convert the rest to webm
        for file in os.listdir(videosDir):
                if file.endswith('.mp4') or file.endswith('.mkv'):
                    # subprocess.run([os.path.dirname(os.path.abspath(__file__)) + "/./convertToWebm.sh", file])
                    pfile = Path(file)
                    subprocess.run(f'ffmpeg -i {file} -c:v libvpx -crf 15 -b:v 1M -c:a libvorbis {pfile.stem}.webm', shell=True, encoding='utf-8')
        # After the conversion, write the new converted filenames to list.txt
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.webm'):
                listFile.write('file ' + '\'' + file + '\'\n')
        # Do the concatenation of WEBM files
        listFile.close()
        subprocess.run('ffmpeg -y -f concat -i list.txt -c copy output.webm', shell=True, encoding='utf-8')

    elif mkvFilesCount > webmFilesCount and mkvFilesCount > mp4FilesCount:
        # Majority MKV files.
        # If the majority is MKV, convert the rest to mkv
        for file in os.listdir(videosDir):
                if file.endswith('.mp4') or file.endswith('.webm'):
                    pfile = Path(file)
                    subprocess.run(f'ffmpeg -i {file} -c:v libx264 -c:a aac {pfile.stem}.mkv', shell=True, encoding='utf-8')
        # After the conversion, write the new converted filenames to list.txt
        for file in sorted(os.listdir(videosDir)):
            if file.endswith('.mkv'):
                listFile.write('file ' + '\'' + file + '\'\n')
        # Do the concatenation of MKV files
        listFile.close()
        subprocess.run('ffmpeg -y -f concat -i list.txt -c copy output.mkv', shell=True, encoding='utf-8')


    # Delete the renamed files
    for file in sorted(os.listdir(videosDir)):
        if file in newFiles:
            os.unlink(file)

    # Remove the list.txt file
    os.unlink('list.txt')



if __name__ == "__main__":
    main()
