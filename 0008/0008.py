__author__ = 'Emma'

# Author: Yue Zhang
# Date:2016-11-25
# Python 3.5

'''
一个HTML文件，找出里面的正文
'''

'''
getBody:从网址中得到所有的正文

Input: url----相应的网址
Output: result----所有的正文内容
'''
import urllib.request
import re
from bs4 import BeautifulSoup

def getBody(url):
    # content=urllib.request.urlopen(url).read()
    # pattern=re.compile('<p>?(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
    # result=pattern.findall(content.decode('GBK'))
    content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content)
    result = soup.body.text
    return result

def main():
    url = 'https://zhidao.baidu.com/question/521343129.html'
    allBody = getBody(url)
    print(type(allBody))
    file = open('htmlbody.txt', 'w+', encoding='gb18030')
    file.write(allBody)
    file.close()

main()

