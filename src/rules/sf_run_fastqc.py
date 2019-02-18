import: "const.py"

rule run_fastqc:
    input:
        target: DATA + 'raw/fastqc'
        sra: DATA + 'raw/fastqc'
    output: DATA + 'interim/fastqc/'
    shell: 'python {SCRIPTS}fastqc.py {input.target} {input.sra} {output}'
