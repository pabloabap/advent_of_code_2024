from typing import List

def asc_desc_checker(report: List[int]) -> int:
	""" 
		Check that all elements in the list are
		in ascending or descending order.
		
		Parameters
		----------
		report: List[int]
			List of numbers
		Returns
		-------
		int
		`1` if `True`, `0` if `False`
	"""
	differ = 0
	for i in range(1, len(report)):
		if (report[i - 1] > report[i]):
			differ -= 1
		elif (report[i - 1] < report[i]):
			differ += 1
		else:
			differ = 0
	return (abs(differ) == len(report) - 1)

def is_safe_report(report: List[int]) -> int:
	""" 
		Check the conditions to classify a report as safe.
		1. The values of the list are all increasing or decreasing.
		2. Any two adjacent numbers differ by at least one and at most three.

		Parameters
		-----------
		report : list[int]
			List of numbers to be checked.
		
		Returns
		-------
		int
			`1` if safe, `0` if unsafe.
	"""
	safe_flag = 1
	ascending = report[0] < report[1]
	if (0 == asc_desc_checker(report)):
		safe_flag = 0
	else:
		for i in range(len(report) - 1):
			if ((ascending and report[i] > report[i + 1]) \
	   			or ((not ascending) and (report[i] < report[i + 1]))):
				safe_flag = 0
				break
			if (1 > abs(report[i] - report[i + 1]) \
	   			or abs(report[i] - report[i + 1]) > 3):
				safe_flag = 0
				break
	return (safe_flag)