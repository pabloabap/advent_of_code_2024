[Day 4 challenge link](https://adventofcode.com/2024/day/4)

# Challenge summary
The [Input file](input.txt) is the same for both challenges.
## Challenge 1
[Input file](input.txt) countain `A` `M` `S` `X` letters in random order. 
You must search `XMAS` word in the file and count the number of occurrences.
`XMAS` word can be horizontal, vertical, diagonal, written backwards, or even 
overlapping other words.

Example:

	> MMMSXXMASM
	> MSAMXMSMSA
	> AMXSXMAAMM
	> MSAMASMSMX
	> XMASAMXAMM
	> XXAMMXXAMA
	> SMSMSASXSS
	> SAXAMASAAA
	> MAMMMXMMMM
	> MXMXAXMASX

Match cases:

	> ....XXMAS.
	> .SAMXMS...
	> ...S..A...
	> ..A.A.MS.X
	> XMASAMX.MM
	> X.....XA.A
	> S.S.S.S.SS
	> .A.A.A.A.A
	> ..M.M.M.MM
	> .X.X.XMASX

**SOLUTION**: `2462`

## Challenge 2
In this case you must match you must search `X-MAX`,
two `MAS` in the shape of an X. Example:
	> M.S
	> .A.
	> M.S

Following the example of the prevous challenge, removing characters that
doesn't follow the new pattern, return a table like:

	> .M.S......
	> ..A..MSMS.
	> .M.S.MAA..
	> ..A.ASMSM.
	> .M.S.M....
	> ..........
	> S.S.S.S.S.
	> .A.A.A.A..
	> M.M.M.M.M.
	> ..........

**SOLUTION**: `1877`
