#!/usr/bin/env python

'''Get all the fasta names filtered by a regex.'''

import argparse
import re

def main():

    # Parse arguments.
    parser = argparse.ArgumentParser(description='Get fasta names filtered.')
    parser.add_argument('-i', '--input', help='indicate input FASTA file', required=True)
    parser.add_argument('-f', '--filter', help='regex to filter, if match filter', type=str,required=True)
    parser.add_argument('-o', '--output', help='indicate output FASTA file', required=True)
    args = parser.parse_args()

    # Open FASTA.
    fasta_in = open(args.input)

    # Create FASTA output file.
    output_file = open(args.output, 'wb')

    # filter regex
    filter = re.compile(args.filter)
    count = 0
    print(args.filter)

    # Parse file and write to output.
    print('Parsing %s...' % args.input)
    for line in fasta_in.readlines():
        if line.startswith('>') and filter.match(line) is not None:
            output_file.write(line[1:])
            count += 1

    # Finish.
    output_file.close()
    fasta_in.close()
    print('Wrote %d fasta names to %s.' % (count, args.output))


if __name__ == '__main__':
    main()
