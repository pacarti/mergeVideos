#! /usr/bin/env bash

file=$1

# Remove the extension from the file
fileNoExt="${file%.*}"

ffmpeg -i "$file" -c:v libx264 -crf 15 -c:a aac "$fileNoExt.mp4"
# bash

exit