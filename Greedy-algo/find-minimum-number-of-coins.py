from os import *
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
	denominations.sort(reverse=True)
	res = 0
	for el in denominations:
		res += amount//el
		amount %= el
	return res


