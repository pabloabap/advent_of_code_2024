import ch1_utils as u1
import ch2_utils as u2

FILE = "./day_2/input.txt"

def challenge_1_resolution() -> int:
	"""
		Open input file, read line by line (each line is a report), check if a 
		report is safe (pass safe conditions):
		1. The values of the list are all increasing or decreasing.
		2. Any two adjacent numbers differ by at least one and at most three.

		Return
		-------
		int: 
			Total count of safe reports.
	"""
	with open(FILE, 'r') as f:
		safe_reports_counter = 0
		line = "\n"
		while (line != ""):
			line = f.readline()
			if (line != ""):
				report = [int(x) for x in line.split(sep=" ")]
				safe_reports_counter += u1.is_safe_report(report)
	return (safe_reports_counter)

def challenge_2_resolution() -> int:
	"""
		Open input file, read line by line (each line is a report), check if a 
		report is safe, pass safe conditions or  if removing a single level 
		from an unsafe report would make it safe to classify it as safe.
		1. The values of the list are all increasing or decreasing.
		2. Any two adjacent numbers differ by at least one and at most three.
		This soltion was handled using `Report` class.

		Return
		-------
		int: 
			Total count of safe reports.
	"""
	with open(FILE, 'r') as f:
		line = "\n"
		while (line != ""):
			line = f.readline()
			if (line != ""):
				report = u2.Report([int(x) for x in line.split(sep=" ")])
				report.is_safe_report()
	return(u2.Report.get_safe_counter())

if __name__ == "__main__":
	print ("CHALLENGE 1 SOLUTION: ", challenge_1_resolution())
	print ("CHALLENGE 2 SOLUTION: ", challenge_2_resolution())