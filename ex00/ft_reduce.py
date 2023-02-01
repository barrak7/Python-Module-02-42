#!/bin/python3

def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	x = iterable[0]
	i = 1
	iterable_len = len(iterable)
	while (i < iterable_len):
		x = function_to_apply(x, iterable[i])
		i += 1

	return x

#some tests

