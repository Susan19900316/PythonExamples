__author__ = 'ZY'
'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成
200 个激活码（或者优惠券）？
'''
'''
分析：产生的激活码：20位，每5位以-连接，字母数字随机
'''
import string,random


'''
iviationForm函数产生StringNumber个英文数字随机产生的字符串

input:
     StringNumber:字符串的个数
Ouput:
    strChar:随机字符串
'''
def iviationForm(StringNumber):
    field=string.ascii_letters+string.digits
    strChar="".join([random.choice(field) for i in range(StringNumber)])
    return strChar

'''
函数功能：产生激活码，激活码由numberStr个strChar通过"-"连接

iput:
    numberStr:一个激活码中strChar的个数
output:
    inviCode:激活码
'''
def iviatationCode(numberStr):
    inviCode="-".join([iviationForm(5) for i in range(numberStr)])
    return  inviCode

'''
multiInviaCode函数功能：产生n个随机的激活码
iput:
    n:激活码个数
output:
    listInviaCode:存放n个激活码的列表
'''
def multiInviaCode(n):
    listInviaCode=[]    #存放激活码
    for i in range(n):
        listInviaCode.append(iviatationCode(4))
    return listInviaCode
'''
def main():
    listInviaCode=multiInviaCode(200)
    for InviaCode in listInviaCode:
        print(InviaCode)

main()
'''
