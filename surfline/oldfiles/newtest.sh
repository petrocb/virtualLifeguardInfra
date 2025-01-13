ffmpeg \
-i "https://cams.cdn-surfline.com/cdn-au/au-midbondi/playlist.m3u8" \
-t 10 \
-c copy /home/ubuntu/surfline/testvideo.mp4
aws s3 cp /home/ubuntu/surfline/testvideo.mp4 s3://beachvids/
