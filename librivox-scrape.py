# librivox-scrape.py
# RSS feeds on LibriVox have numeric id's
# follow each RSS feed to its source page, determine if book is complete and in French
# download all OGG media files

import os, re, urllib2

for index in range(345, 9000):
    if(os.path.exists('librivox/' + str(index))):
        # already crawled
        continue
    os.mkdir('librivox/' + str(index))

    rssPage = urllib2.urlopen('http://librivox.org/rss/' + str(index)).read()

    # eliminate 404 or forum redirects
    if (rssPage.find('We weren\'t able to find that project') > -1 or rssPage.find('Forum Software') > -1):
        continue
    if (rssPage.find('<link>') == -1):
        # not a valid page for reasons that we don't understand
        print("could not interpret " + str(index))
        continue
    print(index)

    # extract main URL
    bookUrl = rssPage[ rssPage.find('<link>') + 15 : rssPage.find('</link>') - 3 ]
    bookPage = urllib2.urlopen(bookUrl).read()

    # filter by language
    language = bookPage[ bookPage.find('<span>Language:') + 22 : ]
    language = language[ : language.find('</p>') ]
    print(language)
    try:
        if (language.lower().find('french') > -1) or (language.lower().find('multilingual') > -1):
            # I want to download this book
            # get the archive.org page
            archiveUrl = bookPage[ bookPage.find('http://www.archive.org/details') : ]
            archiveUrl = archiveUrl[ : archiveUrl.find('Internet Archive Page') - 2 ]
            archivePage = urllib2.urlopen(archiveUrl).read()
            if (archivePage.find('id="vorbis"') == -1):
                print("did not find OGG for this book?")
                continue

            # start downloading each OGG file
            oggFiles = archivePage[ archivePage.find('id="vorbis"') : archivePage.find('All Files') ].split('.ogg')
            for oggPart in oggFiles:
                if (oggPart.find('/download') == -1):
                    # probably last dangling part of the split
                    continue
                oggUrl = "http://www.archive.org" + oggPart[oggPart.find('/download') : ] + ".ogg"
                if len(re.findall(r'_\d+alt_', oggUrl)) > 0:
                    # this is an alternate voice of the same chapter
                    continue
                os.system('wget ' + oggUrl + ' -P librivox/' + str(index) + '/')
    except:
        s = 1
