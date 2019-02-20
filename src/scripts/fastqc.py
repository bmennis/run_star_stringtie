###Script to run fastqc on rnaseq samples for analysis
###code from Apexa Modi in Diskin Lab

#Including const.py for project because contains reference, data, annotation constants for scripts and rules to use
import os, sys
include: "../rules/const.py"

#get the input files and output directory from the arguments passed to the script
#this is new and added for snakemake rules to have input and get output
names = sys.argv[1]
sra = sys.argv[2]
output = sys.argv[3]

#import names of samples from input text file
target_names = open(names, mode = 'r')
#import sra names of samples from input text file
target_sra = open(sra, mode = 'r')

#commenting these output becuase of changes made with inputs provided by snakemake rules
#import names of samples from text file
#target_names = open("TARGET_NBL_Names.txt", mode = 'r')
#import sra names of samples from text file
#target_sra = open("TARGET_NBL_SRA.txt", mode = 'r')

#create arrays from input files to get sample names to run in fastqc
nblArray = target_names.readlines()
sraArray = target_sra.readlines()

#Iterate through each target and sra sample and run fastqc on them
#Updated the fastqc command to output to project data directory in data/interim/fastqc/
for num in range(0, len(nblArray)):
    sraName = sraArray[num].strip()
    nblName = nblArray[num].strip()
    
    print("echo \'fastqc --extract --threads 10 --quiet "+DATA_FASTQ_DISKIN+sraName+".fastq.gz -out "+output+"\' | qsub -cwd -pe smp 10 -N "+nblName)
    os.system("echo \'fastqc --extract --threads 10 --quiet "+DATA_FASTQ_DISKIN+sraName+".fastq.gz -out "+output+"\' | qsub -cwd -pe smp 10 -N "+nblName)

#close the files for the sample names
target_names.close()
target_sra.close()
