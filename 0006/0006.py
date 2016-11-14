__author__ = 'Emma'
'''
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''
import os
import operator

'''
统计文本中的关键字
Input:
    content:文本内容
    KeyNumber:关键字的个数
Output:
    keyWords:关键字所组成的list
'''
def StatisticKeyWord(content,keyNumber):
    contentList = content.split()
    wordList = {}   #用于存储word的字典
    for word in contentList:
        if word in wordList:
            wordList[word] += 1
        else:
            wordList[word] = 1
    sortenWordList = sorted(wordList.items(), key=lambda d:d[1],reverse=True) #按出现的次数降序排列
    keyWords = []   #存放keywords
    for i in range(keyNumber):
        keyWords.append(sortenWordList[i][0])
    return keyWords

def main():
    keyNumber = 4   #日记中关键字的个数
    resoursePath = "D:\\PythonExamples\\0006\\diary"
    assert os.path.exists(resoursePath) #判断路径是否存在
    assert os.path.isdir(resoursePath)  #判断是否是目录
    diaryList = os.listdir(resoursePath)    #日记名字列表
    dicStaKeys = {} #存储每个文件对应的关键字
    for diary in diaryList:
        try:
            file = open(resoursePath+"\\"+diary)
            content = file.read()
            file.close()
            keyWords = StatisticKeyWord(content,keyNumber)
            dicStaKeys[diary] = keyWords

        except Exception as e:
            print("出现问题：")
            print(e)
    print(dicStaKeys)   #输出统计的关键字

main()