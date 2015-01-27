# Haiti Content

Expansions to Internet-in-a-Box

## French language audio for Khan Academy

* Install youtube-dl and ffmpeg
* Run 'yt-user.py KhanAcademyFrancais' to download all of the videos from that user in mp4 format - this process will appear to run immediately, but the downloads take time
* Repeat 'yt-user.py KhanAcademyFrancais' until all of the pages are downloaded
* Run 'yt-to-ogg.py' to convert all of your mp4 videos into ogg/ogv format

If you have problems during video download or conversion, you need to delete MP4 and OGV files instead of expecting the script to overwrite them.
