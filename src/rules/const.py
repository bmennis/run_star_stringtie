import os, sys

p = os.getcwd()
if 'src' in p:
    PWD = p.split('src/')[0]
else:
    PWD = p + '/'

FILES = PWD + 'docs/'
SCRIPTS = PWD + 'src/scripts/'
DATA = PWD + 'data/'
LOG = PWD + 'log/'
CONFIG = PWD + 'configs/'
DATA_FASTQ_DISKIN = '/mnt/isilon/diskin_lab/TARGET_RNA/fastq/'
REF_GENOME_FA_MARIS = '/mnt/isilon/maris_lab/shared_resources/refs/ucsc.hg19.fa'
GENOME_DIR_DISKIN =  '/mnt/isilon/diskin_lab/Apexa/lncRNA_Analysis/STAR-lncRNA-Map/GenomeDir_Gencode101'
GTF_ANNO_DISKIN = '/mnt/isilon/diskin_lab/Apexa/resources/gencode.v19.annotation.gtf' 
