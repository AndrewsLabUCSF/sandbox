import sys

input_files = snakemake.input
output_file = snakemake.output[0]

with open(output_file, 'w') as out:
    for i in input_files:
        sample = i.split('.')[0]
        for line in open(i):
            out.write(sample + ' ' + line)

            