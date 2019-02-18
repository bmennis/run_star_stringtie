###Script to run fastqc on rnaseq samples for analysis
###code from Apexa Modi in Diskin Lab

import os

#import names of samples from text file
names = open("TARGET_NBL_Names.txt", mode = 'r')
#import sra names of samples from text file
sra = open("TARGET_NBL_SRA.txt", mode = 'r')

nblArray = names.readlines()
sraArray = sra.readlines()

for num in range(0, len(nblArray)):
    sraName = sraArray[num].strip()
    nblName = nblArray[num].strip()
    
    print("echo \'fastqc --extract --threads 10 --quiet /home/modia/Diskin_lab/TARGET_RNA/fastq/"+sraName+".fastq.gz -out ./\' | qsub -cwd -pe smp 10 -N "+nblName)
    os.system("echo \'fastqc --extract --threads 10 --quiet /home/modia/Diskin_lab/TARGET_RNA/fastq/"+sraName+".fastq.gz -out ./\' | qsub -cwd -pe smp 10 -N "+nblName)

#close the files for the sample names
names.close()
sra.close()
