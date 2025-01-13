#!/bin/bash

OUTPUT_FILE="/home/ubuntu/videos/swellnet/bondiBeach_$(date +%Y%m%d_%H%M%S).mp4"

ffmpeg -i "https://stream.n1.au.swellnet.com/surfcams/bondi-beach.stream/playlist.m3u8" -t 600 -c copy $OUTPUT_FILE

aws s3 cp $OUTPUT_FILE s3://beachvids3/swellnet/bondi_beach/
rm -f $OUTPUT_FILE
tail -n 300 /home/ubuntu/ffmpeg_log.txt > /home/ubuntu/ffmpeg_log.tmp && mv /home/ubuntu/ffmpeg_log.tmp /home/ubuntu/ffmpeg_log.txt

