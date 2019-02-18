include: "const.py"

rule run_star:
    input: DATA + 'interim/'
    output: DATA + 'interim/'
    shell: 'python {SCRIPTS}star_gencode.py {input} {output}'
