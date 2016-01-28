#!/usr/bin/env python

# This script reads in text files

# Start timing of script
from datetime import datetime
startTime = datetime.now()

# Open one of the fasta files
# Create a list to store data
sequence = []

# Open the file to read ('r')
with open("BRCA1_Homo.sapiens.txt", 'r') as f:
	# For each line
	for line in f:
		# If it starts with '>' (i.e. the first line), skip it
		if line.startswith(">"):
			continue
		else:
			sequence.append(line.strip())

# Turn list into string
sequence = ''.join(sequence)

# Transfer to DNAseq 
DNASeq = sequence

# Count the number of nucleotides (i.e. the length of the string)
nBases = len(DNASeq)

print nBases

# Calculate the percent of each nucleotide
# First determine the unique values using set
Bases = set(DNASeq)
# Empty vector for recording the number of each base
Number = {}

for nucleotide in Bases:
	Number[nucleotide] = DNASeq.count(nucleotide)
	# Calculate proportion of nucleotide
	print "%s: %5.1f" % (nucleotide, 100*Number[nucleotide]/float(len(DNASeq)))

# Print startTime - time to now for estimate of script length
print datetime.now() - startTime
