#!/bin/python3
import csv

class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		if (skip_top < skip_bottom):
			print("ERROR: Skip top value can't be lower that skip bottom")
			exit(1)
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.data = None

	def init_data(self):
		self.data = list(csv.reader(self.fd, delimiter=self.sep))

		length = len(self.data[0])
		for lst in self.data:
			if len(lst) != length:
				return None
		self.data = [list(map(str.strip, lst)) for lst in self.data]
		return True

	def __enter__(self):
		try:
			self.fd = open(self.filename, 'r')
		except FileNotFoundError:
			print(self.filename + ": File does not exist")
			exit(1)
		except PermissionError:
			print(self.filename + ": Permission denied")
			exit(1)
		except:
			print("ERROR")
			exit(1)

		if self.init_data() == None:
			return None

		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		if exc_type is not None:
			print("Something went wrong: {}, {}, {}.".format(exc_type, exc_value, exc_traceback))
		self.fd.close()



	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""

		data = self.data
		length = len(self.data)
		if self.skip_top >= length or self.skip_bottom >= length:
			print("either skip top or skip bottom is out of range")
			exit(1)
		if self.skip_top and self.skip_bottom:
			data = self.data[self.skip_top:self.skip_bottom+1]
		elif self.skip_top and not self.skip_bottom:
			data = self.data[self.skip_top:]
		elif not self.skip_top and self.skip_bottom:
			data = self.data[:self.bottom + 1]

		return data

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		if self.header is True:
			return self.data[0]

