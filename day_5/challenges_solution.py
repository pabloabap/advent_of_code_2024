import re
from collections import defaultdict
import copy as cp

FILE = "./day_5/input.txt"

def challenge_1_resolution() -> int:
	'''
		
	'''
	correct_combinations = []
	dict_comb = {}
	sum_correct = 0
	combinations = re.findall(r'(\d+)\|(\d+)', input)
	for k, v in combinations:
		dict_comb.setdefault(k, []).append(v)
	lists = re.findall(r'(.*,\d+)$',input, re.MULTILINE)
	for list in lists:
		list = re.split(r",", list)
		correct = True
		for n, item in enumerate(list):
			if (n < len(list) - 1):
				if (item not in dict_comb.keys() \
					or str(list[n + 1]) not in dict_comb[item]) :
					correct = False
					break
		if (correct == True):
			correct_combinations.append(list)
	for i in correct_combinations:
		sum_correct += int(i[len(i) // 2])
	return (sum_correct)

def challenge_2_resolution() -> int:
	'''
		
	'''
	incorrect_combinations = []
	dict_comb = {}
	sum_correct_order = 0
	combinations = re.findall(r'(\d+)\|(\d+)', input)
	for k, v in combinations:
		dict_comb.setdefault(k, []).append(v)
	lists = re.findall(r'(.*,\d+)$',input, re.MULTILINE)
	for list in lists:
		list = re.split(r",", list)
		correct = True
		for n, item in enumerate(list):
			if (n < len(list) - 1):
				if (item not in dict_comb.keys() \
					or str(list[n + 1]) not in dict_comb[item]) :
					correct = False
					break
		if (correct == False):
			incorrect_combinations.append(list)
	for comb in incorrect_combinations:
		sorted_result = cp.copy(comb)
		all_items = cp.copy(comb)
		for item in comb:
			counter = 0
			for other in all_items:
				if (item != other and item in dict_comb[other]):
					counter += 1
			sorted_result[counter] = item
		sum_correct_order += int(sorted_result[len(sorted_result) // 2])
	return (sum_correct_order)

if __name__ == "__main__":
	with open(FILE) as f:
		input = f.read()
	print ("CHALLENGE 1 SOLUTION: ", challenge_1_resolution())
	print ("CHALLENGE 2 SOLUTION: ", challenge_2_resolution())