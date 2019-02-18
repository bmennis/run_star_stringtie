###Script to run star with gencode for rnaseq analysis pipeline
###code from Apexa Modi in Diskin lab

import os, sys

##import arguments for samples names
namesFile = sys.argv[2]
##sraFile = sys.argv[2]
target = sys.argv[1]


names = open(namesFile, mode = 'r')
#sra = open(sraFile, mode = 'r')
#namesArray = names.readlines()
#sraArray = sra.readlines()
pathName = "/scr1/users/modia/STAR_Gencode_PanCancer_11918/"+target
os.chdir(pathName)

for files in names.readlines():
        #sraName = sraArray[num].strip()
        #nblName = namesArray[num].strip()
    #print(nblName)
    files = files.strip()
    files = files.split()
    sraName = files[0]
    nblName = files[1]
    os.system("echo \'STAR --runMode alignReads --runThreadN 10 --twopassMode Basic --twopass1readsN -1 --chimSegmentMin 15 --chimOutType WithinBAM --genomeDir /mnt/isilon/diskin_lab/Apexa/lncRNA_Analysis/STAR-lncRNA-Map/GenomeDir_Gencode101  --genomeFastaFiles /mnt/isilon/maris_lab/shared_resources/refs/ucsc.hg19.fa --readFilesIn /mnt/isilon/diskin_lab/TARGET_RNA/fastq/"+sraName+"_1.fastq.gz /mnt/isilon/diskin_lab/TARGET_RNA/fastq/"+sraName+"_2.fastq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /scr1/users/modia/STAR_Gencode_PanCancer_11918/"+target+"/Gencode_"+nblName+". --quantMode TranscriptomeSAM GeneCounts --sjdbGTFfile /mnt/isilon/diskin_lab/Apexa/resources/gencode.v19.annotation.gtf --sjdbOverhang 100\' | qsub -cwd -l mem_free=6G -l m_mem_free=6G -l h_vmem=6G -S /bin/bash -sync n -pe smp 10 -e STAR-Gencode_"+nblName+".error -o STAR-Gencode_"+nblName+".error -N "+nblName)
    print("echo \'STAR --runMode alignReads --runThreadN 10 --twopassMode Basic --twopass1readsN -1 --chimSegmentMin 15 --chimOutType WithinBAM --genomeDir /mnt/isilon/diskin_lab/Apexa/lncRNA_Analysis/STAR-lncRNA-Map/GenomeDir_Gencode101  --genomeFastaFiles /mnt/isilon/maris_lab/shared_resources/refs/ucsc.hg19.fa --readFilesIn /mnt/isilon/diskin_lab/TARGET_RNA/fastq/"+sraName+"_1.fastq.gz /mnt/isilon/diskin_lab/TARGET_RNA/fastq/"+sraName+"_2.fastq.gz --readFilesCommand zcat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix /scr1/users/modia/STAR_Gencode_PanCancer_11918/"+target+"/Gencode_"+nblName+". --quantMode TranscriptomeSAM GeneCounts --sjdbGTFfile /mnt/isilon/diskin_lab/Apexa/resources/gencode.v19.annotation.gtf --sjdbOverhang 100\' | qsub -cwd -l mem_free=6G -l m_mem_free=6G -l h_vmem=6G -S /bin/bash -sync n -pe smp 10 -e STAR-Gencode_"+nblName+".error -o STAR-Gencode_"+nblName+".error -N "+nblName) 
    #os.system("echo 'samtools view -h Gencode_"+nblName+".Aligned.sortedByCoord.out.bam | awk -v strType=2 -f tagXSstrandedData.awk | samtools view -bS - > Gencode_"+nblName+"_XS.Aligned.sortedByCoord.out.bam' | qsub -cwd -N addXS_"+nblName)
    #print("echo 'samtools view -h Gencode_"+nblName+".Aligned.sortedByCoord.out.bam | awk -v strType=2 -f tagXSstrandedData.awk | samtools view -bS - > Gencode_"+nblName+"_XS.Aligned.sortedByCoord.out.bam' | qsub -cwd -N "+nblName)

##close the files for the samples
names.close()
#sra.close()
