#! /usr/bin/env bash

file=$1

# Remove the extension from the file
fileNoExt="${file%.*}"

# echo "file with extension: $file"
# echo "file without extension: $fileNoExt"
# echo "file with MP4 extension: $fileNoExt.mp4"

ffmpeg -y -i "$file" -c:v copy -c:a copy "$fileNoExt.mkv"