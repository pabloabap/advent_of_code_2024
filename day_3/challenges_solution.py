import re

FILE = "./day_3/input.txt"

def challenge_1_resolution() -> int:
	'''
		Open and read input file, search `mult(x,y)` pattern 
		(been `X` and `Y` 1 to 3 digits numbers), multiply `X` and `Y`
		and sum all the results.

		Return:
		--------
		int:
			Result of multiplications sum.
	'''
	result = 0
	with open(FILE, 'r') as f:
		input = f.read()
		mults=re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)
		for i in mults:
			i = re.findall(r'\d{1,3}', i)
			result += int(i[0]) * int(i[1])
	return(result)

def challenge_2_resolution() -> int:
	'''
		Open and read input file, search pattern `do()` and `don't,
		generate a sequence of ocurrences list and a list spliting
		the input by these ocurrences, iterate the spliting list and
		if in the first item or after `do()` and match `mult(x,y)` pattern 
		(been `X` and `Y` 1 to 3 digits numbers), multiply `X` and `Y`
		and sum all the results.

		Return:
		--------
		int:
			Result of multiplications sum.
	'''
	result = 0
	with open(FILE, 'r') as f:
		input = f.read()
		do_dont_seq = re.findall(r"do\(\)|don't\(\)", input)
		do_dont_items = re.split(r"do\(\)|don't\(\)", input)
		for i, val in enumerate(do_dont_items):
			if (i == 0 or do_dont_seq[i - 1] == 'do()'):
				mults=re.findall(r'mul\(\d{1,3},\d{1,3}\)', val)
				for j in mults:
					j = re.findall(r'\d{1,3}', j)
					result += int(j[0]) * int(j[1])
	return(result)

if __name__ == "__main__":
	print ("CHALLENGE 1 SOLUTION: ", challenge_1_resolution())
	print ("CHALLENGE 2 SOLUTION: ", challenge_2_resolution())