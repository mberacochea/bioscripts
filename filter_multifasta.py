#!/usr/bin/env python
 
'''Filer a multifasta by lenght.'''

import argparse

 
def main():
    '''Execute.'''
 
    # Parse arguments.
    parser = argparse.ArgumentParser(description='Filter a Multi-FASTA files.', epilog='Get the filtered fastas.')
    parser.add_argument('-i', '--input', help='indicate input FASTA file', required=True)
    parser.add_argument('-l', '--len', help='Min length', type=int, default=1000)
    parser.add_argument('-o', '--output', help='indicate output FASTA file', required=True)
    args = parser.parse_args()
 
    # Open FASTA.
    fasta_in = open(args.input)
 
    # Create FASTA output file.
    fasta_out = open(args.output, 'wb')

    # Min len
    length = args.len

    # Parse file and write to output.
    print('Parsing %s ' % args.input)

    # current fasta
    current_header = ''
    current = ''
    for line in fasta_in.readlines():       
        if line.startswith('>'):
            # write the current seq if longer than
            if len(current) > length:
                fasta_out.write(current_header + current)
            # new seq
            current_header = line
            current = ''
        else:
            current += line
 
    # Finish.
    # write the last seq if longer than
    if len(current) > length:
        fasta_out.write(current_header + current)

    fasta_out.close()
    fasta_in.close()
    print('Wrote fastas longer than %d to %s.' % (length, args.output))


if __name__ == '__main__':
    main()
