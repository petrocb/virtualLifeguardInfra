#!/bin/bash

OUTPUT_FILE="/home/ubuntu/videos/surfline/southBondi_$(date +%Y%m%d_%H%M%S).mp4"

ffmpeg -i "https://cams.cdn-surfline.com/cdn-au/au-southbondi/playlist.m3u8" \
-t 600 \
-c copy $OUTPUT_FILE

aws s3 cp $OUTPUT_FILE s3://beachvids3/surfline/south_bondi/
rm -f $OUTPUT_FILE
tail -n 300 /home/ubuntu/ffmpeg_log.txt > /home/ubuntu/ffmpeg_log.tmp && mv /home/ubuntu/ffmpeg_log.tmp /home/ubuntu/ffmpeg_log.txt
