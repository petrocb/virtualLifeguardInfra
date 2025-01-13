#!/bin/bash

OUTPUT_FILE="/home/ubuntu/videos/testvid2.mp4"

ffmpeg -i "https://cams.cdn-surfline.com/east-au/au-bondinorth/playlist.m3u8" \
-t 10 \
-c copy $OUTPUT_FILE

aws s3 cp $OUTPUT_FILE s3://beachvids/
rm -f $OUTPUT_FILE
tail -n 300 /home/ubuntu/ffmpeg_log.txt > /home/ubuntu/ffmpeg_log.tmp && mv /home/ubuntu/ffmpeg_log.tmp /home/ubuntu/ffmpeg_log.txt

