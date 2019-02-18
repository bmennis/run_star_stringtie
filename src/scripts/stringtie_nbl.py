###Script to run stringtie on RNAseq samples for analysis 
###code from Apexa Modi in Diskin lab

import os
import sys
#make compatible with DESeq + discover denovo transcripts
#names = open("/home/modia/Apexa/lncRNA_Analysis/TARGET_NBL_Names.txt", mode = 'r')
#sra = open("/home/modia/Apexa/lncRNA_Analysis/TARGET_NBL_SRA.txt", mode = 'r')


directory = sys.argv[1]

nblArray = os.listdir(directory)
#os.chdir(directory)

for files in nblArray:
    if files[-21:] == "sortedByCoord.out.bam":
        nblName = files[0:-22]
        print("mkdir ./ballgown/stringtie_"+nblName)
        print("echo \'stringtie /scr1/users/modia/STAR_Gencode_Stringtie/NBL/"+nblName+".sortedByCoord.out.bam -G /home/modia/Apexa/resources/gencode.v19.annotation.gtf -B -o ./ballgown/stringtie_"+nblName+"/stringtie_"+nblName+"_out.gtf -A ./ballgown/stringtie_"+nblName+"/"+nblName+"_gene_abund.tab -C ./ballgown/stringtie_"+nblName+"/"+nblName+"_cov_refs.gtf -p 10\' | qsub -cwd -l mem_free=5G -l m_mem_free=5G -l h_vmem=5G -S /bin/bash -sync n -pe smp 10 -e StringTie_"+nblName+".error -o StringTie_"+nblName+".txt")
        #os.system("mkdir ./ballgown/stringtie_"+nblName)
        #os.system("echo \'stringtie /scr1/users/modia/STAR_Gencode_Stringtie/Gencode_"+nblName+".Aligned.sortedByCoord.out.bam -G /home/modia/Apexa/resources/gencode.v19.annotation.gtf -B -o /scr1/users/modia/StringTie_NBL/ballgown/stringtie_"+nblName+"/stringtie_"+nblName+"_out.gtf -A /scr1/users/modia/StringTie_NBL/ballgown/stringtie_"+nblName+"/"+nblName+"_gene_abund.tab -C /scr1/users/modia/StringTie_NBL/ballgown/stringtie_"+nblName+"/"+nblName+"_cov_refs.gtf -p 5\' | qsub -cwd -l mem_free=5G -l m_mem_free=5G -l h_vmem=5G -S /bin/bash -sync n -pe smp 5 -e StringTie_"+nblName+".error -o StringTie_"+nblName+".txt")
    #os.system("echo \'stringtie Gencode_"+nblName+".Aligned.sortedByCoord.out.bam -G /home/modia/Apexa/resources/gencode.v19.annotation.gtf -B -o /home/modia/Apexa/ballgown/stringtie_"+nblName+"/stringtie_"+nblName+"_out.gtf -A "+nblName+"_gene_abund.tab -C "+nblName+"_cov_refs.gtf -c 0 -p 5\' | qsub -cwd -l mem_free=5G -l m_mem_free=5G -l h_vmem=5G -S /bin/bash -sync n -pe smp 5 -e StringTie_"+nblName+".error -o StringTie_"+nblName+".txt")

##Close the files for the samples
names.close()
sra.close()
