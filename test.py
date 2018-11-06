#!/usr/bin/python
import fileinput
import glob
#for file in glob.glob("/home/akshata/1M/*.text"):
		 open("randwrite1M.text") as infile:
			for line in infile:
				if "read :" in line:
					sub_line = line.split(",")
					sub_sub_line = sub_line[2].split("=")
				 	print(', '.join(sub_sub_line))
						
  				        
