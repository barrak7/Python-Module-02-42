#!/bin/python3

class TinyStatistician:
	@staticmethod
	def mean(x):
		if not x:
			return
		m = len(x)
		if not isinstance(x, list) or m == 0 or not all([isinstance(e, (int, float)) for e in x]):
			return
		value = 0
		for element in x:
			value += element

		return value / m

	@staticmethod
	def median(x):
		if not x:
			return
		m = len(x)
		if not isinstance(x, list) or m == 0 or not all([isinstance(e, (int, float)) for e in x]):
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
		m = len(x)
		if not isinstance(x, list) or m == 0 or not all([isinstance(e, (int, float)) for e in x]):
			return
		x.sort()
		values = [TinyStatistician.median(x[:int(m/2)]), TinyStatistician.median(x[int(m/2):])]
		return values

	@staticmethod
	def var(x):
		if not x:
			return
		m = len(x)
		if not isinstance(x, list) or m == 0 or not all([isinstance(e, (int, float)) for e in x]):
			return
		x.sort()
		med = TinyStatistician.median(x)
		value = 0
		for element in x:
			value += (element - m) * (element - m)
		return float(value / 2)

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
# Expected result: 82.4
print(tstat.median(a))
# Expected result: 42.0
print(tstat.quartile(a))
# Expected result: [10.0, 59.0]
print(tstat.var(a))

