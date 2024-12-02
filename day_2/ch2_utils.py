from typing import List
import copy


class Report:
	"""
		A class used to represent a Report (list of levels)

		Class Attributes
		----------------
		safe_counter: int
			Count the number of reports that are safe.
		
		Instance Attributes
		-------------------
		levels: List[int]
			List of integers representing levels.
		safe_flag: int
			Flag to know if the instance is a safe report or not (1: Yes, 0: No).
			Set to 0 by default.
		asc_flag: int
			Flag to know if the instance is sorted ascendent (1) or descendent (0).
			Set to 1 by default.
		
		Methods
		--------
	"""
	safe_counter = 0

	def __init__(self, levels: List[int]):
		"""
		Parameters
		-----------
		levels: List[int]
			List of integers representing levels.
		"""
		self.levels = levels
		self.safe_flag = 0
		self.asc_flag = 1

	@classmethod
	def get_safe_counter(cls) -> int:
		"""
			Class method to get the number of safe reports, `safe_counter`.
		"""
		return (cls.safe_counter)
	

	def asc_desc_checker(self, tmp_levels) -> int:
		""" 
			Check that all elements in the list are
			in ascending or descending order.
			
			Parameters
			----------
			tmp_levels: List[int]
				List of numbers
			Returns
			-------
			int
			`1` if `True`, `0` if `False`
		"""
		differ = 0
		for i in range(1, len(tmp_levels)):
			if (tmp_levels[i - 1] > tmp_levels[i]):
				differ -= 1
			elif (tmp_levels[i - 1] < tmp_levels[i]):
				differ += 1
			else:
				differ = 0
		return (abs(differ) == len(tmp_levels) - 1)

	def is_safe_report(self):
		""" 
			Check the conditions to classify a tmp_levels as safe.
			1. The values of the list are all increasing or decreasing.
			2. Any two adjacent numbers differ by at least one and at most three.

			Parameters
			-----------
			tmp_levels : list[int]
				List of numbers to be checked.
			
			Returns
			-------
			int
				`1` if safe, `0` if unsafe.
		"""
		for i in range(len(self.levels) + 1):
			if (self.safe_flag == 0):
				tmp_levels = copy.deepcopy(self.levels)
				if (i < len(self.levels)):
					del tmp_levels[i - 1]
				ascending = tmp_levels[0] < tmp_levels[1]
				if (1 == self.asc_desc_checker(tmp_levels)):
					self.safe_flag = 1
					for i in range(len(tmp_levels) - 1):
						if ((ascending and tmp_levels[i] > tmp_levels[i + 1]) \
							or ((not ascending) and (tmp_levels[i] < tmp_levels[i + 1]))):
							self.safe_flag = 0
							break
						if (1 > abs(tmp_levels[i] - tmp_levels[i + 1]) \
							or abs(tmp_levels[i] - tmp_levels[i + 1]) > 3):
							self.safe_flag = 0
							break
			else:
				break

		Report.safe_counter += self.safe_flag