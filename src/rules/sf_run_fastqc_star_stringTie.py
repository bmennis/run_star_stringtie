###snakefile that contains rules to run fastqc, STAR, and stringTie for pipeline
###this file includes const.py which contains variable for pathways and files for 
###ref genomes, annotations, and sample files
include: "const.py"

#The fastqc rule takes in a list of SRA names and TARGET, the script then pulls
#the names from the files to select the corresponding sample fastq files.
#The output is written to the project data/ directory
rule run_fastqc:
    input:
        target: DATA + 'raw/fastqc',
        sra: DATA + 'raw/fastqc'
    output: DATA + 'interim/fastqc/'
    shell: 'python {SCRIPTS}fastqc.py {input.target} {input.sra} {output}'

#The STAR rule takes in a list of SRA names and the script will pull the 
#sample fastq files with the SRA names to run through STAR. The reference files
#and the annotation files are pulled from variables defined in const.py.  Any changes
#to the annotations or references should be changed there.  The output from STAR is written to 
#the project data/interim/ directory
rule run_star:
    input: DATA + 'interim/'
    output: DATA + 'interim/'
    shell: 'python {SCRIPTS}star_gencode.py {input} {output}'

#The stringTie rule
rule run_stringTie:
    input: DATA + 'interim/'
    output: DATA + 'interim/'
    shell: 'python {SCRIPTS}stringtie_nbl.py {input} {output}'
