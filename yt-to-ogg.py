# yt-to-ogg.py
# use ffmpeg to convert mp4 videos to ogv

import os

localFiles = os.listdir('./')
for file in localFiles:
    if (file.find('.mp4') == len(file) - 4):
        # is an mp4 and not mp4.part file
        ogvName = file.replace(".mp4", ".ogv")
        if (ogvName not in localFiles):
            # hasn't yet been converted
            os.system("ffmpeg -i " + file.replace(" ", "\\ ") + " -c:v libtheora -c:a libvorbis -q:v 7 -q:a 7 " + ogvName.replace(" ", "\\ "))
