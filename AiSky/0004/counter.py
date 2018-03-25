#!/usr/bin/env python3
# -*-coding:utf-8-*-
__author__ = 'ArianX/arianx.me'

#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

import string
from collections import Counter

class CountWords():
	def __init__(self):
		self.words = None
		self.sorting_words = None

	def load_file(self, filename):
		'''
		Pass a filename whose words will be counted later.
		'''
		file = open(filename, 'rt')
		str_trans = str.maketrans('', '', string.punctuation)
		self.words = []
		for line in file.readlines():
			per_line_words = line.strip().translate(str_trans).split()
			self.words.extend(per_line_words)

		file.close()
		return True

	def counter(self, order=0):
		'''
		Set order to 1 for a ascending order, or a descending order.Default order is descending.
		'''
		if self.words==None:
			print('You must read the file first.')
			return False

		counter = Counter(self.words)
		self.sorting_words = counter.most_common(len(counter))

		if order:
			self.sorting_words.reverse()

		return True

	def clear(self):
		'''
		The method will clear up all of the resource in the instance.
		'''
		self.wrods = None
		self.sorting_words =None

if __name__=='__main__':
	counter = CountWords()
	counter.load_file('test.txt')
	counter.counter()

	print('All of the words in the file:\n', counter.words)
	print('After the sorting of the words:\n', counter.sorting_words)