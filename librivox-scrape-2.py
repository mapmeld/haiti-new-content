import os

downloaded = os.listdir('librivox')

for download in downloaded:
	if download.find('.') == -1 and len(os.listdir('librivox/' + download)) > 0:
		# has French or Multilingual content
		print(download)
	else:
		os.system('rm -r librivox/' + download)
