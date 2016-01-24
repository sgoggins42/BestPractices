#!/usr/bin/env python

# Best practices example script
# This is the first version with the sequence written into the script

DNASeq = "ATGTCTCATTCAAAGSCA"

# Count the number of nucleotides (i.e. the length of the string)
nBases = len(DNASeq)

print nBases


# Count the number of nucleotides by using a counter
BaseCounter = 0
for base in DNASeq:
	BaseCounter += 1

print BaseCounter

