include: 'const.py'

rule run_stringTie:
    input: DATA + 'interim/'
    output: DATA + 'interim/'
    shell: 'python {SCRIPTS}stringtie_nbl.py {input} {output}'
