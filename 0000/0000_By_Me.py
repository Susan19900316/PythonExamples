__author__ = 'ZY'

from PIL import ImageFont, ImageDraw, Image
import sys,random,os

num=str(random.randint(1,99))  #随机产生1-99间的任意整数,然后转换为字符串
imagePath=os.path.join(sys.path[0],'mio.jpg')  #图片存储路径
savePath=os.path.join(sys.path[0],'mio_numbei.jpg') #图片存储路径

def addNumberToImge(im, font, wDraw, hDraw):
    draw=ImageDraw.Draw(im) #提取图像信息
    draw.text((wDraw,hDraw), num, font=font, fill='red')
    im.save(savePath,'jpeg')

def main():
    im=Image.open(imagePath)    #打开图像
    w,h=im.size   #图像的长宽
    print('Orginal image size is %sx%s'%(w,h))
    #数字的起始位置
    wDraw=int(w*0.8)
    hDraw=int(w*0.02)
    font=ImageFont.truetype('arial.ttf',30) #数字的mode和大小
    addNumberToImge(im, font, wDraw, hDraw)

main()




