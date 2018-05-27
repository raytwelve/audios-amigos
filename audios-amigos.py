
# audio playing on platform is broken down into many smaller audio files with a m3u file as a playlist with the http link to each audio segment
# This program takes in the m3u file and finds each http link and downloads the file 
# note: url links in m3u file uses session_id that expire

import requests
import os


#method used to download file
def get_file(dest_name, src_url):
    with open(dest_name, 'ab') as handle:
        response = requests.get(src_url, stream=True)
#        if not response.ok:
#            print (response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)


#search directory for m3u files
infiles = []
for file in os.listdir("./"):
    if file.endswith(".m3u"):
    	infiles.append(file)

# specify destination directory
d = ""

plist = 0;
for f in infiles:
	plist += 1
	fname = ""
	if plist < 10:
		fname = "0"
	fname += str(plist) + ".mp3"

	infile = open(f, "r")
	contents = infile.read()

	fdir_fname = d + fname

	for entry in contents.split('\n'):
		if(entry.startswith("https")):
			get_file(fdir_fname, entry)

	infile.close()


