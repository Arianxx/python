#!/usr/bin/env python3
# -*-coding:utf-8-*-
__author__ = 'ArianX/arianx.me'

# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont

class picWriter():

	def __init__(self):
		self.pic = None
		self.font = None
		self.ins = None

	def open(self, filename):
		self.pic = Image.open(filename)
		return True

	def close(self):
		self.pic.close()
		return True

	def setFont(self, fontname, size):
		self.font = ImageFont.truetype(fontname, size)
		return True

	def draw(self, text, color):
		self.ins = ImageDraw.Draw(self.pic)
		position = (self.pic.size[0] - self.font.size * 0.7, 0)
		self.ins.text(position, text, font=self.font, fill=color)
		self.pic.show()
		self.pic.save(text+'.png')
		return True

if __name__=='__main__':
	pic = picWriter()
	pic.open('init.jpg')
	pic.setFont('Arial.ttf', 100)
	pic.draw('4', 'red')
	pic.close()