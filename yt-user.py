# yt-user.py
# Use youtube-dl (https://github.com/rg3/youtube-dl) to download all of a user's videos

import sys, urllib2, json, os

def downloadUserVideos(ytUser, localFiles, start=1):
    # get their JSON feed (gets first few videos)
    videoFeed = json.loads(urllib2.urlopen("http://gdata.youtube.com/feeds/base/users/" + ytUser + "/uploads?alt=json&v=2&orderby=published&start-index=" + str(start)).read())
    foundAnyNewVideos = False
    for video in videoFeed["feed"]["entry"]:
        videoUrl = video["link"][0]["href"]
        videoId = videoUrl[videoUrl.find("v=") + 2 : ]
        if videoId.find("&") > -1:
            videoId = videoId[ : videoId.find("&")]

        finishedDownload = False
        for file in localFiles:
            file = file.decode('utf-8')
            if (file.find(videoId + ".mp4") == len(file) - 4 - len(videoId)):
                # this video already finished downloading
                finishedDownload = True
                break
        if finishedDownload:
            continue
        else:
            foundAnyNewVideos = True

        print("downloading " + videoUrl)
        os.system("youtube-dl " + videoUrl)

    if not foundAnyNewVideos:
        if len(videoFeed["feed"]["entry"]) < 25:
            # end of all pages
            return
        # grab next page
        print("checking next page")
        downloadUserVideos(ytUser, localFiles, start + 25)

def main(argv):
    # get the YouTube User
    ytUser = argv[0]

    # get local MP4 files
    localFiles = os.listdir("./")

    downloadUserVideos(ytUser, localFiles)

if __name__ == "__main__":
    main(sys.argv[1:])
