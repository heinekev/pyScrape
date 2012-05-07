# depravity.py

import urllib, os

x = 0

for x in range (0,9999):
	# append zero space (image naming scheme)
	formatted = '%0*d' % (4, x)

	# create URL string
	url = 'http://www.your_url_here.com/IMG_' + str(formatted) + ".JPG"

	# test for response code
	response = urllib.urlopen(url)
	if response.code == 200:
		print 'success: ' + url
		urllib.urlretrieve(url, str(formatted) + ".jpg")
	else:
		print 'failure: ' + str(formatted)
		
