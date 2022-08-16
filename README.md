# GFF3-feature-exporter
Python script that extracts information from a GFF3 file. 

GFF (general feature format) files are tab-delimited files that store information on biological features. More information can be read here: https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md

This script takes in four long arguments on the command line:
* --source_gff=/path/to/.gff3 file 
* --type=
* --attribute=
* --value=

If the feature is found, the FASTA sequence of that feature will be printed to the terminal.
