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

* Don't delete your MP4 files! You will need them for Android devices and older browsers.

### Enabling OGG playback in KA-Lite

* Add these changes to allow and prefer OGG video format in KA-Lite: https://github.com/mapmeld/ka-lite/commit/ebf31e68122ef3548a6ef0f8b9e321ef812b74b3

### Troubleshooting

If you have problems during video download or conversion, you need to delete MP4 and OGV files instead of expecting the script to overwrite them.

If you missing any of the OGV files, and your browser supports OGV, it will error instead of switching to MP4 format. Only apply the KA-Lite changes if you are committed to OGG format.

## Public domain French audiobooks from Librivox

Run librivox-scrape.py to start searching all Librivox recordings for French audiobooks

The code will skip any books which do not have 'French' in the languages list, and wget any OGG files from the associated Archive.org page into a directory.
