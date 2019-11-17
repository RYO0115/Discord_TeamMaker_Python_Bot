
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from PIL import Image, ImageDraw, ImageFont

class DRAW_SHAPE():
    def __init__(self, image_name):
        self.size_x = 512
        self.size_y = 512
        self.image_name = image_name
        self.SetConfigure()

    def SetConfigure(self):
        self.SetRectangleSize()
        self.SetRectangleFillColor()
        self.SetEllipseFillColor()
        self.SetLineFillColor()
        self.SetEdgeColor()
        self.SetTextSize()
        #self.GetNewImage()

    def GetCenterPoint(self):
        return([self.size_x/2, self.size_y/2])

    def SetCenterPoint(self, x, y):
        self.size_x = x * 2
        self.size_y = y * 2


    def GetNewImage(self):
        self.im = Image.new("RGB",(int(self.size_x), int(self.size_y )),(255,255,255))
        self.draw = ImageDraw.Draw(self.im)


    def SetRectangleSize(self, dx=100, dy=20):
        self.rectangleXSize = dx
        self.rectangleYSize = dy

    def SetRectangleFillColor(self, color="white"):
        self.recColor = color

    def SetLineFillColor(self, color="black"):
        self.lineColor = color

    def SetEllipseFillColor(self, color="white"):
        self.ellipseColor = color

    def SetEdgeColor(self, color="Black"):
        self.edgeColor = color

    def DrawRectangle(self, x, y):
        self.draw.rectangle([(x,y),( x+self.rectangleXSize, y+self.rectangleYSize)], fill=self.recColor, outline=self.edgeColor, width=2)

    def DrawLine(self, x1,y1, x2, y2, width):
        self.draw.line((x1,y1,x2,y2), fill=self.lineColor, width=width)

    def DrawZigZagXtoY(self, x1, y1, x2, y2, width=10):
        self.DrawLine(x1,y1,x2,y1, width)
        self.DrawLine(x2,y1,x2,y2, width)

    def DrawZigZagYtoX(self, x1, y1, x2, y2, width=10):
        self.DrawLine(x1,y1,x1,y2, width)
        self.DrawLine(x1,y2,x2,y2, width)


    def DrawEllipse(self, x1,y1, x2,y2):
        self.draw.ellipse(( x1, y1, x2, y2), fill=self.ellipseColor, outline=self.edgeColor)

    def SetTextSize(self, textSize=10):
        self.textSize = textSize

    def SetModestTextSize(self, char, targetWidth):
        width = self.textSize * len(char)
        if width < targetWidth:
            self.textSize = targetWidth / len(char)

    def SetFontSize(self):
        self.font = ImageFont.truetype(size=self.textSize)

    def SetImageSize(self, x, y):
        self.size_x = x
        self.size_y = y

    def DrawText(self, x1, y1, text):
        #draw = ImageDraw.Draw(self.im)
        #self.SetFontSize()
        self.draw.multiline_text((x1,y1), text, font=self.font, fill=(0,0,0,255))

    def SetFontFile(self, fontFileName, size=10):
        fileDir = os.path.dirname(os.path.abspath(__file__)) + "/../font/" + fontFileName
        self.font = ImageFont.truetype(fileDir, size)


    def ShawImage(self):
        self.im.show()

    def SaveImage(self):
        img_dir = os.path.dirname(os.path.abspath(__file__)) + "/../../image/"
        if os.path.exists(img_dir):
            ret = 1
        img = img_dir + self.image_name + ".jpg"
        self.im.save(img)
        return img

if __name__=='__main__':
    ds = DRAW_SHAPE("sample")
    ds.DrawRectangle(30,30)
    ds.DrawText(33,30,"brabra")
    ds.ShawImage()
