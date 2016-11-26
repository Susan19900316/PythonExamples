__author__ = 'Emma'

# Author: Yue Zhang
# Date: 2016-11-26
# Python3.5
'''
In a file html, find all the links in it
'''

import urllib.request
from bs4 import BeautifulSoup
import re

'''
function: to get all the urls in the html
Input: url---the html link
Output: result---all the links in the html
'''

def getUrl(url):
    content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content)
    result = soup.findAll('a')
    # r = re.compile('src=".*?" | src=\'.*?\'')
    # result = r.findall(content.decode('GBK'))
    return result

def main():
    url = "http://xh.5156edu.com/html2/h14.html"
    allUrls = getUrl(url)
    file = open('Urls.txt','w')  # The text to save the urls into
    for eachUrl in allUrls:
        file.write(eachUrl['href']+'\n')  # Write the url into the text
    file.close()

main()


