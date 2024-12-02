[Day 2 challenge link](https://adventofcode.com/2024/day/2)

# Challenge summary
## Challenge 1
[Input file](input.txt) consists of many reports, one **report per line**. Each 
**report is a list of numbers called levels that are separated by spaces**.

Only some reports are safe, your program must **return the number of safe reports**. 
The conditions to classify a report as save are:
- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.

Examples:
- `7 6 4 2 1`: **Safe** because the levels are all decreasing by 1 or 2.
- `1 2 7 8 9`: **Unsafe** because 2 7 is an increase of 5.
- `9 7 6 2 1`: **Unsafe** because 6 2 is a decrease of 4.
- `1 3 2 4 5`: **Unsafe** because 1 3 is increasing but 3 2 is decreasing.
- `8 6 4 4 1`: **Unsafe** because 4 4 is neither an increase or a decrease.
- `1 3 6 7 9`: **Safe** because the levels are all increasing by 1, 2, or 3.

**SOLUTION**: `559`

## Challlenge 2
Same rules apply as before, except if removing a single level from an unsafe 
report would make it safe, the report instead counts as safe.

**SOLUTION**: `601`
