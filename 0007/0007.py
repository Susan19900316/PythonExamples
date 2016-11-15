__author__ = 'Emma'
# -*- coding: utf-8 -*-

'''
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import os
import chardet

'''
统计代码中的代码、空行、注释行的数目
Input:
    codeContent- 代码内容
Output:
    CodeNumber - 代码的行数
    NullNumber - 空行的行数
    NoteNumber - 注释的行数
'''
def statisticCode(codeContent):
    codeNumber = 0
    nullNumber = 0
    noteNumber = 0
    noteFlagBe = 0
    lineList = codeContent.splitlines() #按行分开
    for line in lineList:
        if line == '':  #空行
            nullNumber += 1
        else:
            wordList = line.split() #每行的每个单词
            if wordList[0][0] == '#':
                noteNumber += 1
                continue
            else:
                for word in wordList:
                    if noteFlagBe == 1 and word != "'''":
                        noteNumber += 1
                        break
                    if word == "'''":
                        if noteFlagBe == 1:
                            noteFlagBe = 0
                            noteNumber += 1
                        else:
                            noteFlagBe = 1
                            noteNumber += 1
                            continue
                    else:
                        codeNumber += 1
                        break

    return codeNumber,nullNumber,noteNumber

def main():
    resourcePath = "D:\\测试"
    assert os.path.exists(resourcePath)
    assert os.path.isdir(resourcePath)
    codeList = os.listdir(resourcePath) #存放代码名称
    codeDic = {"Code": 0, "Null": 0, "Note": 0}    #存放代码，空行和注释的行数
    for code in codeList:
        try:
            file = open(resourcePath+'\\'+code,'rb')
            codeContent = file.read().decode('utf-8')
            file.close()
            CodeNumber,NullNumber,NoteNumber = statisticCode(codeContent)
            codeDic["Code"] += CodeNumber
            codeDic["Null"] += NullNumber
            codeDic["Note"] += NoteNumber
        except Exception as e:
            print("出现问题：")
            print(e)
    print(codeDic)
main()