#!/bin/python3

import time
from random import randint
import os

def log(func):
	def inner(*args):
		with  open("machine.log", "a") as log_file:
			start = time.perf_counter()
			x = func(*args)
			t = time.perf_counter() - start
			unit = "s"
			if t < 1:
				unit = "ms"
				t = t * 1000
			log_file.write("({})Running: {} [ exec-time = {:.3f} {}]\n".format(os.getenv("USER", "UNKOWN"), func.__name__.replace('_', ' ').title().ljust(20), t, unit))

		return x
	return inner

class CoffeeMachine():
	water_level = 100

	@log
	def start_machine(self):

		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for e in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":

	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()

	machine.make_coffee()
	machine.add_water(70)
