#! /usr/bin/env bash

file=$1

# Remove the extension from the file
fileNoExt="${file%.*}"

# echo "file with extension: $file"
# echo "file without extension: $fileNoExt"
# echo "file with MP4 extension: $fileNoExt.mp4"

ffmpeg -y -i "$file" -c:v libvpx -crf 15 -b:v 1M -c:a libvorbis "$fileNoExt.webm"