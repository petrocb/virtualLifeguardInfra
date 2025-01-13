ffmpeg \
-i "https://cams.cdn-surfline.com/cdn-au/au-bondiramp2/playlist.m3u8" \
-t 10 \
-c copy /home/ubuntu/surfline/testvideo.mp4
aws s3 cp /home/ubuntu/surfline/testvideo.mp4 s3://beachvids/

#"https://cams.cdn-surfline.com/cdn-au/au-midbondi/playlist.m3u8"
#"https://hls.cdn-surfline.com/east-au/au-bondiramp2/playlist.m3u8"
