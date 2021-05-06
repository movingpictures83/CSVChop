# CSVChop
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: CSV (indexed)
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that returns a slice of a CSV file, indexed by
a starting and ending row.

The plugin accepts as input a parameter file of keyword-value pairs:
csvfile: The input CSV file
start: Starting index for the slice (0 assumed if not specified)
end: Ending index for the slice (last row assumed if not specified)

The output CSV file will be rows of the input csvfile between index
start and end
