#!/usr/bin/env python3
# -*-coding:utf-8-*-
__author__ = 'ArianX/arianx.me'

# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random, string

def geneCode(filename, length, num):
	file = open(filename, 'wt')
	chars = string.ascii_letters + string.digits
	for a in range(num):
		code = ''.join(['-'+random.choice(chars) if index%5==0 and index!=0 else random.choice(chars) for index in range(length)])
		print(code)
		file.write(code+'\n')
	return True

if __name__=='__main__':
	geneCode('code.txt', 20, 200)