#!/usr/bin/env python3

import csv
import sys

SEP = "\t"

class Mapper(object):

	def __init__(self, infile=sys.stdin, separator=SEP):
		self.infile = infile
		self.sep = separator

	def emit(self, key, value):
		sys.stdout.write(f"{key}{self.sep}{value}\n")

	def map(self):
		pair = []
		
		for row in self:
			pair = [row[3], row[4]]
			self.emit(row[1], pair)

	def __iter__(self):
		for row in csv.reader(self.infile):
			yield row


if __name__ == '__main__':
 	mapper = Mapper()
 	mapper.map()
