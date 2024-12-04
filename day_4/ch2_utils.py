import re
from typing import List

def x_mas_searcher(lines: List[str]) -> int:
	""" 
		
	"""
	matches = 0
	r, c = len(lines), len(lines[0])
	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if ((i > 0 and i < (r - 1)) and (j > 0 and j < (c - 1))):
				if (char == 'A'):
					if (lines[i - 1][j - 1] == 'M' \
		 				and lines[i + 1][j + 1] == 'S' \
						and	lines[i - 1][j + 1] == 'M' \
						and	lines[i + 1][j - 1] == 'S' ):
						matches += 1
					elif (lines[i - 1][j - 1] == 'S' \
		 				and lines[i + 1][j + 1] == 'M' \
						and	lines[i - 1][j + 1] == 'S' \
						and	lines[i + 1][j - 1] == 'M' ):
						matches += 1
					elif (lines[i - 1][j - 1] == 'M' \
		 				and lines[i + 1][j + 1] == 'S' \
						and	lines[i - 1][j + 1] == 'S' \
						and	lines[i + 1][j - 1] == 'M' ):
						matches += 1
					elif (lines[i - 1][j - 1] == 'S' \
		 				and lines[i + 1][j + 1] == 'M' \
						and	lines[i - 1][j + 1] == 'M' \
						and	lines[i + 1][j - 1] == 'S' ):
						matches += 1
	return (matches)