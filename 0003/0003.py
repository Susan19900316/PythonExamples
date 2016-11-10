__author__ = 'ZY'
'''
任一个英文的纯文本文件，统计其中的单词出现的个数。
'''

'''
统计输入内容的单词数
Input :
    content--文本内容
Output:
    wordNumber--单词数量
'''
def count(content):
    wordList = content.split()
    wordNumber = len(wordList)
    return wordNumber
def main():
    file = open('test.txt')
    content = file.read()
    wordNumber = count(content)
    print("单词数是:",wordNumber)
    file.close()
main()