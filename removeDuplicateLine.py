#!/usr/bin/python

import sys

inputFile = sys.argv[1]
outFile = inputFile + ".rdl"

fin = open(inputFile)
fout = open(outFile, 'w')

index = 0;

for line in fin.readlines():
	index = index + 1;
	line = line.strip()
	if index % 3 == 0:
			fout.write(line + "\n")
	
		
fin.close()
fout.close()
