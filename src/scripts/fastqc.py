###Script to run fastqc on rnaseq samples for analysis
###code from Apexa Modi in Diskin Lab

import os, sys
include: "../rules/const.py"

#get the input files and output directory from the arguments passed to the script
names = sys.argv[1]
sra = sys.argv[2]
output = sys.argv[3]

#import names of samples from input text file
target_names = open(names, mode = 'r')
#import sra names of samples from input text file
target_sra = open(sra, mode = 'r')

#import names of samples from text file
#target_names = open("TARGET_NBL_Names.txt", mode = 'r')
#import sra names of samples from text file
#target_sra = open("TARGET_NBL_SRA.txt", mode = 'r')

nblArray = target_names.readlines()
sraArray = target_sra.readlines()

#Iterate through each target and sra sample and run fastqc on them
#Updated the fastqc command to output to project data directory in data/interim/fastqc/
for num in range(0, len(nblArray)):
    sraName = sraArray[num].strip()
    nblName = nblArray[num].strip()
    
    print("echo \'fastqc --extract --threads 10 --quiet "+DATA_DISKIN+sraName+".fastq.gz -out "+output+"\' | qsub -cwd -pe smp 10 -N "+nblName)
    os.system("echo \'fastqc --extract --threads 10 --quiet "+DATA_DISKIN+sraName+".fastq.gz -out "+output+"\' | qsub -cwd -pe smp 10 -N "+nblName)

#close the files for the sample names
target_names.close()
target_sra.close()
