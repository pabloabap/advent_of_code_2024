import ch1_utils as u1
import ch2_utils as u2

FILE = "./day_4/input.txt"

def challenge_1_resolution() -> int:
	'''
		Open and read input file, search `XMAS` or `SAMX` word in all directions
		(horizonta, vertical, diagonal up and diagonal down), count matches
		on each direction and sum all.

		Return:
		--------
		int:
			Total counter of `XMAS` occurrences.
	'''
	with open(FILE, 'r') as f:
		read = f.read()
		lines = read.split("\n")
	return(u1.horizontal_matches(lines) + u1.vertical_matches(lines) + 
		u1.diagonal_down_matches(lines) + u1.diagonal_up_matches(lines))

def challenge_2_resolution() -> int:
	'''
		Open and read input file, search `MAS` or `SAM` word in all directions
		(horizonta, vertical, diagonal up and diagonal down), count matches
		on each direction and sum all.

		Return:
		--------
		int:
			Total counter of `MAS` occurrences.
	'''
	with open(FILE, 'r') as f:
		read = f.read()
		lines = read.split("\n")
	return(u2.x_mas_searcher(lines))
if __name__ == "__main__":
	print ("CHALLENGE 1 SOLUTION: ", challenge_1_resolution())
	print ("CHALLENGE 2 SOLUTION: ", challenge_2_resolution())