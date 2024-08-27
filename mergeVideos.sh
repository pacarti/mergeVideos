#! /usr/bin/env bash

path="$@"

python3 mergeVideos.py "$path"

ffmpeg -y -f concat -i "$path/list.txt" -c copy "$path/output.webm"

bash
