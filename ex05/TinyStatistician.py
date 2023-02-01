#!/bin/python3

import math

class TinyStatistician:
	@staticmethod
	def mean(x):
		if not x:
			return
		if not isinstance(x, list) or not all([isinstance(e, (int, float)) for e in x]):
			return
		m = len(x)
		if m == 0:
			return
		value = 0
		for element in x:
			value += element

		return value / m

	@staticmethod
	def median(x):
		if not x:
			return
		if not isinstance(x, list) or not all([isinstance(e, (int, float)) for e in x]):
			return
		m = len(x)
		if m == 0:
			return
		x = sorted(x)
		if m % 2 == 0:
			if (m / 2 + 1) < m:
				return float((x[int(m / 2)] + x[int(m / 2) + 1]) / 2)
			else:
				return float((x[int(m / 2)] + x[int(m / 2)]) / 2)
		return float(x[int(m / 2)])

	@staticmethod
	def quartile(x):
		if not x:
			return
		if not isinstance(x, list) or not all([isinstance(e, (int, float)) for e in x]):
			return
		m = len(x)
		if m == 0:
			return
		x.sort()
		if m % 2 == 0:
			values = [TinyStatistician.median(x[:m//2]), TinyStatistician.median(x[m//2:])]
		else:
			values = [TinyStatistician.median(x[:m//2 + 1]), TinyStatistician.median(x[m//2:])]
		return values

	@staticmethod
	def var(x):
		if not x:
			return
		if not isinstance(x, list) or not all([isinstance(e, (int, float)) for e in x]):
			return
		m = len(x)
		if m == 0:
			return
		x.sort()
		med = TinyStatistician.mean(x)
		value = 0
		for element in x:
			value += (element - med) ** 2
		return float(value / m)

	@staticmethod
	def std(x):
		if not x:
			return
		if not isinstance(x, list) or not all([isinstance(e, (int, float)) for e in x]):
			return
		m = len(x)
		if m == 0:
			return
		value = TinyStatistician.var(x)
		return math.sqrt(value)

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
# Expected result: 82.4
print(tstat.median(a))
# Expected result: 42.0
print(tstat.quartile(a))
# Expected result: [10.0, 59.0]
print(tstat.var(a))
# Expected result: 12279.439999999999
print(tstat.std(a))
# Expected result: 110.81263465868862
