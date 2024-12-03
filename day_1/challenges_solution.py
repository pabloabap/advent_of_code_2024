import pandas as pd
from collections import Counter

def challenge_1_resolution(df: pd.DataFrame) -> int:
	"""
		Sort the two columns of input.txt ascending,
		get the distance for each pair of numbers (in absolute values) and 
		sum the results to get the total discane. 
		Example: `1`in first column and `3` in second column and the oposite, 
		return the same discance of `2`.

		Parameteres
		------------
		`df` (pd.DataFrame): The dataframe that contain the two columns.

		Return
		-------
		int: The sum of absolute differences between two columns sorted
		ascending.
	"""
	df[0] = df[0].sort_values(ascending=True).values
	df[1] = df[1].sort_values(ascending=True).values
	total_abs_distance = int(abs(df[0] - df[1]).sum())
	return(total_abs_distance)

def challenge_2_resolution(df: pd.DataFrame) -> int:
	"""
		Count how many times a unique number of the `left column` appear in the
		`right column`, multiply each value by its counter and sum the result 
		to get the `total_similarity_score`.

		Parameteres
		------------
		df: pd.DataFrame
			The dataframe that contain the two columns.

		Return
		-------
		int: 
			Sum of multiplication of each unique number of the left column by 
			the number of times it appears in the second column.
	"""
	unique_left_values = df[0].unique().tolist()
	right_values_in_unique_left_values = df[1][df[1].isin(unique_left_values)]
	count_unique_right_values = Counter(right_values_in_unique_left_values)
	total = sum(key * value for key, value in count_unique_right_values.items())
	return(total)
	

if __name__ == "__main__":
	df = pd.read_csv("./day_1/input.txt", sep = "   ", header=None, \
				engine='python')
	print (challenge_1_resolution(df))
	print (challenge_2_resolution(df))
	