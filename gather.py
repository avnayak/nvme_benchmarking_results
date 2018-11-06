#!/usr/bin/python
import glob

#for filenames in glob.glob("home/akshata/gather4K/*.text"):
filenames=['rr4K.text','rrw4K.text','rw4K.text','sqr4K.text','sqw4K.text']
readers=[open(filename) for filename in filenames]
for lines in zip(*readers):
	print('\t'.join([line.strip() for line in lines]))

