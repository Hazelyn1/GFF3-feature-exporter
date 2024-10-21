# GFF3-feature-exporter
Python script that extracts information from a GFF3 file. 

GFF (general feature format) files are tab-delimited files that store information on biological features. More information can be read here: https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md

This script takes in four long arguments on the command line:
* --source_gff=/path/to/.gff3 file 
* --type=
* --attribute=
* --value=

If the feature is found, the FASTA sequence of that feature will be printed to the terminal.

The program begins with importing the necessary libraries and assigning five variables:
args - empty list that stores the four command line long arguments
seqid - stores sequence id of FASTA sequence, intially set as an empty string
flag - checks if feature of choice is found, set to "FALSE" intially, meaning the feature is not yet found
i - tracks how many matches are found in the GFF file. If i>1, then more than one match is found
fasta_seq - if feature is found in GFF file, this variable stores the corresponding FASTA sequence

Before the GFF file can be searched, the long argument the user inputs on the command line must be parsed using the "getopt" function and assigned appropriately to the "args" variable using the "append" function. Since "args" is a list, the arguments must be converted to strings for use in the program and since there are four arguments, these were hard-coded to the "arg1", "arg2", "arg3" and "arg4" variables using the ".join" function.

Once the arguments are read in properly processed to indicate what the user is looking for in the file, the GFF file can be opened using the "open" function. In order for a feature to be found in the file, all four arguments must match and the file is traversed line by line. This is accomplished using a for loop and nested if statement conditionals.
If the current line of the file contains the feature of interest, say a gene, which was assigned to "arg2", it advances to the next if statement checking for "arg3", which is an attribute of the feature, say the ID value. If this is found, then it advance further to find the specific value of the attribute specified in "arg3" (which is stored in "arg4"), like a FASTA sequence ID. This search is accomplished using regex. If this value is found, it's stored in the "seqid" variable. 
In the GFF file, columns 4 and 5 provide the start and end positions of the feature in the FASTA sequence. In order to extract the proper sequence segment in the FASTA sequence, these positions are stored in separate variables for future use and "i" is incremented by one to indicate that a match has been found. 

If "i" is exactly equal to one, then another if statement (still inside the for loop) is entered. This conditional checks that a sequence id has been registered in the "seqid" variable and that the header of the FASTA sequence of interest begins with the ">" token. Nested within this if statement there is another conditional that checks if the current line in the file contains the proper header and if not than to continue to the next line. 
Once the correct header is found for the FASTA sequence, if the feature is found on just a single line of the FASTA file (i.e. <60 characters), then the corresponding sequence is stored in the "fasta_seq" variable, the flag is set to "TRUE", the loop gets broken, and the correct FASTA sequence is printed to the terminal. 
In the case that the sequence feature is longer than one line (i.e. >60 characters), then the "seq_lines" variable calculates how many lines the feature consists of, parses through the correct number of lines in the FASTA sequence, assigns them to the "fasta_seq" variable, sets the flag to "TRUE", breaks out of the loop, and prints the correct FASTA sequence to the terminal. 

At the very end of the program, in the case that i = 0, "No match found" will be printed to the terminal. In the case that i>1, indicating that multiple matches for the same feature were found in the file, the program will print "Multiple matches found" to the terminal.

End of program.

