__author__ = 'Emma'
'''
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
'''
import os
from PIL import Image

#判读是否为图片
def judgeImage(image):
    filename=os.path.splitext(image)
    fPostfix=filename[1]
    if (fPostfix !='.jpg' and fPostfix !='.png' and fPostfix != '.JPG' and fPostfix != '.PNG'):
        print("该文件不是图像！")
        return False
    else:
        return True


#检查图片分辨率的大小，并使其小于max,min
def modifyResolution(pathDir,hight,weight):
    assert os.path.exists(pathDir)
    assert os.path.isdir(pathDir)  #判断是否为目录
    imageList = os.listdir(pathDir)
    count=0 #改变数目计数
    for image in imageList:
        if(judgeImage(image)==True):    #是图像
            try:
                img=Image.open(pathDir+"\\"+image)
            except:
                print("打开上述图像错误，请检查")
                continue
            imsize=img.size   #求图像分辨率
            if (imsize[0]>hight or imsize[1]>weight):
                count+=1
                newing=img.resize((min(hight,imsize[0]),min(imsize[1],weight)))
                newing.save(pathDir+"\\"+str(count)+".jpg")
            img.close()




def main():
    pathDir='F:\\手绘图片'
    hight=1136
    weight=640
    modifyResolution(pathDir,hight,weight)

main()