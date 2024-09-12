#! /usr/bin/env bash

file=$1

# Remove the extension from the file
fileNoExt="${file%.*}"

ffmpeg -i "$file" -c:v libvpx -crf 15 -b:v 1M -c:a libvorbis "$fileNoExt.webm"
# bash

exit