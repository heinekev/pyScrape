# threadscrape.py
# now with threads!
# -----------------
# the entire purpose of this script is to iteratively scrape a web server for a given file
# in this case:  IMG_xxxx.JPG
# I define the range (0 through 9999) and divide the work up into 8 threads
# This is here for posterity and adaptability
# 
# Kevin Anderson 5/6/2012

import urllib, os, threading

# Defining the worker process.  Takes two arguments (in this case, integers)       
def worker(start,finish):
	
	for x in range (start,finish):
		
		# define your URL here.  I'm concatenating a string
		# using a deprecated form if integer formatting '%0*d' % (4, x)
		# YMMV.  This extends the integer to 4 characters filling in the space with 0s 
		# in accordance with the IMG_xxxx.JPG naming scheme		
		url = 'http://www.your_url_here.com/IMG_' + str('%0*d' % (4, x)) + ".JPG"
		
		# gather and check the HTTP response code here (todo: exception handling)
		response = urllib.urlopen(url)
		if response.code == 200:
			print threading.currentThread().getName() + ' success: ' + url
			
			# download the image to the current working directory
			urllib.urlretrieve(url, "IMG_" + str('%0*d' % (4, x)) + ".jpg")
		else:
			print threading.currentThread().getName() + ' failure: ' + str('%0*d' % (4, x))

# this is a messy hack to divide up work among threads somewhat evenly
# this doesn't scale well and definitely has issues with remainders
start = 0
end = 9999
numthreads = 8
threads = []

# here there be dragons
for x in range(0,numthreads):
	
	# check if this is the first pass
	# set up initial values
	if x == 0:
		newend = end / numthreads
		
		# create new thread, pass in start/end values
		t = threading.Thread(target=worker, args=(start,newend))
		threads.append(t)
		t.start()
		
		# set up the next threads starting position
		start = newend + 1 
	else:
		newend = start + end / numthreads
		
		# create new thread, pass in start/end values
		t = threading.Thread(target=worker, args=(start,newend))
		threads.append(t)
		t.start()
		
		# set up the next threads starting position
		start = newend + 1