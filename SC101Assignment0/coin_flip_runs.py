"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO：主要是執硬幣，連續正面或反面算一次，需要總共n遍連續才算完成
	"""
	print("Let's flip a coin!")
	n = int(input("Number of runs: "))
	roll1 = r.randint(1, 2)
	print(reverse(roll1), end='')
	run = 0
	can_add = True
	while True:
		roll2 = r.randint(1, 2)
		if roll1 == roll2:
			if can_add:
				run += 1
				can_add = False
			else:
				can_add = True
				if run == n:
					break
		roll1 = roll2
		print(reverse(roll2), end='')


def reverse(s):
	if s == 1:
		return 'T'
	if s == 2:
		return "H"
	else:
		pass

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #


if __name__ == "__main__":
	main()
