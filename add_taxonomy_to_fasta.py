#!/usr/bin/env python

'''Add the taxonomy to fasta file name, using the output of qiime assing_taxonomy.py.'''

import argparse

def main():

    # Parse arguments.
    parser = argparse.ArgumentParser(description='Add the taxonomy to fasta.')
    parser.add_argument('-i', '--input', help='input FASTA file', required=True)
    parser.add_argument('-t', '--tax', help='assing_taxonomy.py output', type=str,required=True)
    parser.add_argument('-o', '--output', help='output FASTA file', required=True)
    args = parser.parse_args()

    # Parse the taxonomies file - build a dict with { seq-name: tax }
    tax_file = open(args.tax)
    seq_tax = {}
    split = ""
    for line in tax_file.readlines():
        split = line.split('\t')
        seq_tax[split[0].strip()] = split[1].strip()
    tax_file.close()

    # Create FASTA output file
    output_file = open(args.output, 'wb')

    # Parse fasta and write to output.
    fasta_in = open(args.input)
    for line in fasta_in.readlines():
        if line.startswith('>'):
            output_file.write(seq_tax[line.strip()])
            count += 1
        else:
            output_file.write(line)

    # Finish.
    output_file.close()
    fasta_in.close()
    print('Done')


if __name__ == '__main__':
    main()
