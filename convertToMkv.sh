#! /usr/bin/env bash

file=$1

# Remove the extension from the file
fileNoExt="${file%.*}"

ffmpeg -i "$file" -c:v libx264 -c:a aac "$fileNoExt.mkv"
# bash

exit