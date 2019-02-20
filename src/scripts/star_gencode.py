###Script to run star with gencode for rnaseq analysis pipeline
###code from Apexa Modi in Diskin lab

#Add import of const.py so that can refer to reference and annotation paths and files
import os, sys
include: "../rules/const.py"

##import arguments for samples names
namesFile = sys.argv[2]
##sraFile = sys.argv[2]
target = sys.argv[1]


names = open(namesFile, mode = 'r')
#sra = open(sraFile, mode = 'r')
#namesArray = names.readlines()
#sraArray = sra.readlines()

#Removing the pathname and change of path because does not appear to be used
#Also removing because will write output to project data directory
#pathName = "/scr1/users/modia/STAR_Gencode_PanCancer_11918/"+target
#os.chdir(pathName)

#Iterate through names file and get both sra and nbl names to pull samples to run through STAR
for files in names.readlines():
        #sraName = sraArray[num].strip()
        #nblName = namesArray[num].strip()
    #print(nblName)
    files = files.strip()
    files = files.split()
    sraName = files[0]
    nblName = files[1]
#Commands to run STAR which will pull reference genome, genome fa file, and gtf annotation path and file from const.py
#Also from conts.py will pull the directory for fastq files in diskin lab directory and will write output to local project
#directory data/interim/target_name/gencode_nbl_name
    os.system("echo \'STAR --runMode alignReads --runThreadN 10 --twopassMode Basic --twopass1readsN -1 --chimSegmentMin 15 --chimOutType WithinBAM --genomeDir "+GENOME_DIR_DISKIN+" --genomeFastaFiles "+REF_GENOME_FA_MARIS+" --readFilesIn "+DATA_FASTQ_DISKIN+sraName+"_1.fastq.gz "+DATA_FASTQ_DISKIN+sraName+"_2.fastq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix "+DATA+"interim/"+target+"/Gencode_"+nblName+". --quantMode TranscriptomeSAM GeneCounts --sjdbGTFfile "+GTF_ANNO_DISKIN+" --sjdbOverhang 100\' | qsub -cwd -l mem_free=6G -l m_mem_free=6G -l h_vmem=6G -S /bin/bash -sync n -pe smp 10 -e STAR-Gencode_"+nblName+".error -o STAR-Gencode_"+nblName+".error -N "+nblName)
    print("echo \'STAR --runMode alignReads --runThreadN 10 --twopassMode Basic --twopass1readsN -1 --chimSegmentMin 15 --chimOutType WithinBAM --genomeDir "+GENOME_DIR_DISKIN+"  --genomeFastaFiles "+REF_GENOME_FA_MARIS+" --readFilesIn "+DATA_FASTQ_DISKIN+sraName+"_1.fastq.gz "DATA_FASTQ_DISKIN+sraName+"_2.fastq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix "+DATA+"interim/"+target+"/Gencode_"+nblName+". --quantMode TranscriptomeSAM GeneCounts --sjdbGTFfile "+GTF_ANNO_DISKIN+" --sjdbOverhang 100\' | qsub -cwd -l mem_free=6G -l m_mem_free=6G -l h_vmem=6G -S /bin/bash -sync n -pe smp 10 -e STAR-Gencode_"+nblName+".error -o STAR-Gencode_"+nblName+".error -N "+nblName) 
    #os.system("echo 'samtools view -h Gencode_"+nblName+".Aligned.sortedByCoord.out.bam | awk -v strType=2 -f tagXSstrandedData.awk | samtools view -bS - > Gencode_"+nblName+"_XS.Aligned.sortedByCoord.out.bam' | qsub -cwd -N addXS_"+nblName)
    #print("echo 'samtools view -h Gencode_"+nblName+".Aligned.sortedByCoord.out.bam | awk -v strType=2 -f tagXSstrandedData.awk | samtools view -bS - > Gencode_"+nblName+"_XS.Aligned.sortedByCoord.out.bam' | qsub -cwd -N "+nblName)

##close the files for the samples
names.close()
#sra.close()
