#!/usr/bin/env python3
# -*-coding:utf-8-*-
__author__ = 'ArianX/arianx.me'

#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import MySQLdb

class StoreCode():
	def __init__(self):
		self.file = None
		self.conn = None
		self.cursor = None

	def load_file(self, filename):
		try:
			self.file = open(filename, 'rt')
		except IOError:
			print("An error occurred trying to read the file.")
			self.file = None
			return False

		return True

	def connect_mysql(self, user, passwd, db='test', host='127.0.0.1', port=3306):
		try:
			conn = MySQLdb.connect(user=user, passwd=passwd, db=db, host=host, port=port)
		except MySQLdb.Error:
			print("Can't connect to the mysql.")
			return False

		self.conn = conn
		self.cursor = conn.cursor()
		return True

	def store_code(self):
		if self.cursor==None:
			print("You haven't got the mysql connection.")
			return False
		if self.file==None:
			print("You haven't loaded the code file")
			return False

		query_exist_table = 'SHOW TABLES IN test'
		self.cursor.execute(query_exist_table, [])
		results = self.cursor.fetchall()
		table_exist = False
		for result in results:
			if 'codelist' in result:
				table_exist = True
				break
		if not table_exist:
			query_create_table = 'CREATE TABLE `test`.`codelist` \
								(`id` INT NOT NULL AUTO_INCREMENT, \
								`code` VARCHAR(25) NOT NULL,PRIMARY KEY (`id`));'
			self.cursor.execute(query_create_table, [])

		query_insert_code = 'INSERT INTO test.codelist (code) VALUES(%s);'
		for code in self.file:
			code = code.strip()
			self.cursor.execute(query_insert_code, [code, ])

		self.conn.commit()
		return True

	def load_code_from_mysql(self):
		if self.cursor==None:
			print("You haven't got the mysql connection.")
			return False

		query_get_code = 'SELECT code from test.codelist'
		self.cursor.execute(query_get_code, [ ])
		results = self.cursor.fetchall()
		codelist = []
		for code in results:
			codelist.append(code)
			print(code)

		return codelist

	def clear_resource(self):
		if self.file:
			self.file.close()
			self.file = None
		if self.cursor:
			self.cursor.close()
			self.conn.close()
			self.cursor = None
			self.conn = None
			self.dbname = None

		return True

if __name__=='__main__':
	store = StoreCode()
	store.load_file('code.txt')
	store.connect_mysql(user='root', passwd='', db='test')
	store.store_code()
	store.load_code_from_mysql()
	store.clear_resource()

