import re
from typing import List

def	horizontal_matches(lines: List[str]) -> int:
	""" 
		Search `XMAS` word in each line, written in
		right or inverted order and count ocurrences.
		
		Parameters
		----------
		lines: List[str]
			List of strings/sentences.
		Returns
		-------
		int
			Count of all horizontal occurences.
	"""
	matches = 0
	lista = []
	for line in lines:
		lista.append(len(line))
		matches += len(re.findall(r"XMAS", line))
		matches += len(re.findall(r"SAMX", line))
	return (matches)

def vertical_matches(lines: List[str]) -> int:
	""" 
		Search `XMAS` word in each new line, composed by characters
		in the same position in all sentences, written in
		right or inverted order and count all ocurrences.
		
		Parameters
		----------
		lines: List[str]
			List of strings/sentences.
		Returns
		-------
		int
			Count of all horizontal occurences.
	"""
	matches = 0
	for i in range(len(lines[0])):
		h_line = ""
		for j in range(len(lines)):
			h_line += lines[j][i]
		matches += len(re.findall(r"XMAS", h_line))
		matches += len(re.findall(r"SAMX", h_line))
	return (matches)


def diagonal_down_matches(lines: List[str]) -> int:
	""" 
		Search `XMAS` word in each new line, composed by positive diagonal 
		characters, written in right or inverted order and count all 
		ocurrences.
		Example of positive diagonal characters joining:
		///
		///
		///

		Parameters
		----------
		lines: List[str]
			List of strings/sentences.
		Returns
		-------
		int
			Count of all diagonal down occurences.
	"""
	matches = 0
	r, c = len(lines), len(lines[0])
	d_lists = ["" for _ in range(r + c - 2)]
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if (i + j < len(d_lists)):
				d_lists[ i + j ] += char
	for list in d_lists:
		matches += len(re.findall(r"XMAS", list))
		matches += len(re.findall(r"SAMX", list))
	return (matches)
			
def diagonal_up_matches(lines: List[str]) -> int:
	""" 
		Search `XMAS` word in each new line, composed by negative diagonal 
		characters, written in right or inverted order and count all 
		ocurrences.
		Example of positive diagonal characters joining:
		\\\\
		\\\\
		\\\\

		Parameters
		----------
		lines: List[str]
			List of strings/sentences.
		Returns
		-------
		int
			Count of all up diagonal occurences.
	"""
	matches = 0
	r, c = len(lines), len(lines[0])
	d_lists = ["" for _ in range(r + c)]
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if (i + j < len(d_lists)):
				d_lists[ (r + c) // 2 - (j - i) ] += char
	for list in d_lists:
		matches += len(re.findall(r"XMAS", list))
		matches += len(re.findall(r"SAMX", list))
	return (matches)