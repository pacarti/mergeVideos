#! /usr/bin/env bash

path="$@"


if [[ "$path" == */ ]] ; then
    path=${path::-1}
fi

python3 mergeVideos.py "$path"
exit_code=$?

if [[ "$path" == '' ]] ; then
    printf "Please specify the path with video files!\nSyntax: mergeVideos.sh path/to/videofiles\n"
fi

case $exit_code in
    0)
        echo "sys exit 0"
        ;;
    1) # Folder contains MP4 video files only
        ffmpeg -y -f concat -i "$path/list.txt" -c copy "$path/output.mp4"
        ;;
    2) # Folder contains WEBM video files only
        ffmpeg -y -f concat -i "$path/list.txt" -c copy "$path/output.webm"
        ;;
    3) # Folder contains MKV video files only
        ffmpeg -y -f concat -i "$path/list.txt" -c copy "$path/output.mkv"
        ;;
    
esac
# bash

exit