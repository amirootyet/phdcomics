#!/usr/bin/python

"""The PhD Comics Downloader"""
"""
This code fetches PhD comics from www.phdcomics.com
and saves to '/root/'

Written by: Pranshu
bajpai [dot] pranshu [at] gmail [dot] com

""" 


from bs4 import BeautifulSoup
from urllib import urlretrieve
import urllib2
import re

for i in range(1, 1699):

    url = "http://www.phdcomics.com/comics/archive.php?comicid=%d" %i 
    html = urllib2.urlopen(url)
    content = html.read()
    soup = BeautifulSoup(content)

    for image in soup.find_all('img', src=re.compile('http://www.phdcomics.com/comics/archive/' + 'phd.*gif$')):
        print "[+] Fetched Comic " + "%d" %i + ": " + image["src"]
    outfile = "/root/" + "%d" %i + ".gif"
    urlretrieve(image["src"], outfile)
