#!/usr/bin/python3
#Hazelyn Cates

import sys
import getopt
import re

args = [] #empty list to store arguments
seqid = "" #store fasta sequence id, originally set as an empty string
flag = False #check if feature is found, set to False, meaning it is NOT found
i = 0 #this is for checking if more than one match is found in the file. If this >1, then more than one match is found
fasta_seq = "" #store correct fasta sequence

#Read in long option arguments
options, arguments = (getopt.getopt(sys.argv[1:], "", ['source_gff=', 'type=', 'attribute=', 'value=']))

#print(options)

for options, arguments in options:
	args.append(arguments.split("=")) #read the arguments (which come after the "=") into a list 
	 
#print(args) #this prints the arguments list
#print(args[0]) #can access each of them using its index

#Convert the list items to strings in order to use them as variables in the program:
arg1 = ''.join(args[0])
arg2 = ''.join(args[1])
arg3 = ''.join(args[2])
arg4 = ''.join(args[3])

#print(arg2) #prints the correct thing for each variable given the passed arguments
	
open_file = open(arg1, "r")
#print(open_file) 

for line in open_file:
	new_line = line.strip()
	#print(new_line) #this correctly prints the file
	
	if arg2 in new_line:
	
		if arg3 in new_line:
			#print(sys.argv[3])
			#now want to get the value of the ID 
			if arg4 in new_line:
				print(">%s:%s=%s" % (arg2, arg3, arg4))
				#print(new_line) #This selects the proper line in the file given all the arguments
				
				#want to figure out the seqid (column 1) to determine which FASTA sequence to look for
				#Use regex and start at the beginning of "new_line" and stop at the first tab
				seq_id = re.search(r"^(.+?)\s", new_line)
				if seq_id:
					seqid = seq_id.group()
					#print(seqid) #Stores the first column ONLY
				
				#Now want to extract the start and end positions, which are NOT arguments
				#Use regex to find the numbers
				position_pat = re.search(r"(\d+)\t(\d+)", new_line)
				
				if position_pat:
					start_pos = position_pat.group(1)
					end_pos = position_pat.group(2)
					#convert start and end positions to integers:
					start_pos = int(start_pos) - 1
					end_pos = int(end_pos) + 1
					#print(start_pos)
					#print(end_pos)
					i+=1 #increment i by 1 if feature is found
				continue
	
	if i == 1: #meaning only one feature was found:
		if seqid != "": #want to check if string is empty. If it is, go back through the file to the next line. 
			        #if not, get the sequence corresponding to that feature
			header = (">" + seqid) #this is the header of the specific FASTA sequence
			header = header.strip()
			#print(header)
	
			if new_line.startswith(header):				
				#want to keep reading the lines of the file until the end position is hit
				
				if end_pos < 60: #this would check if the end position is on the first line of the sequence
					fasta_seq = next(open_file).strip()
					flag = True #if it is, set the flag to true, break out of the loop, and print the sequence
					break
				
				else: #if not, want to keep reading the file until the index of the end position is reached
					seq_lines = int(end_pos / 60) + 1 #this calculates how many lines of sequence to look through, instead of 											looking through all of them. Round up to next whole number
					
					for line in range(0, seq_lines): #only iterate through the lines needed given the start and end positions 
						flag = True			
						fasta_seq += next(open_file) 
						
					break
														

if i > 1:
	print("Multiple matches found")
	
elif flag == True:
	print(fasta_seq[start_pos:end_pos])
	
else:
	print("No match found")
					
					
