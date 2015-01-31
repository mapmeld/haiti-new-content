# Haiti Content

Expansions to Internet-in-a-Box

## French language video for Khan Academy

### Using KA-Lite

* Install KA-Lite, log in as admin, download French language pack, and set server language to French
* Start automated download of all French language videos through KA-Lite
* Install ffmpg, using options --with-theora --with-vorbis

### Alternative: downloading from YouTube

* Install youtube-dl and ffmpeg, using options --with-theora --with-vorbis
* Run 'yt-user.py KhanAcademyFrancais' to download all of the videos from that user in mp4 format - this process will appear to run immediately, but the downloads take time
* Repeat 'yt-user.py KhanAcademyFrancais' until all of the pages are downloaded (up to 500)
* Change uploaded sort to other sorts

### Converting downloaded MP4s to OGG

* Run 'yt-to-ogg.py' to convert all of your mp4 videos into ogg/ogv format

### Troubleshooting

If you have problems during video download or conversion, you need to delete MP4 and OGV files instead of expecting the script to overwrite them.

