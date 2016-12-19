#!/usr/bin/env python
 
'''Slice a fasta by position'''

from Bio import SeqIO
import argparse

def main():
    '''Execute.'''
 
    # Parse arguments.
    parser = argparse.ArgumentParser(description="Slice a fasta files.", epilog="Get the filtered fastas.")
    parser.add_argument("-i", "--input", help="indicate input FASTA file", required=True)
    parser.add_argument("-s", "--start", help="Start", type=int)
    parser.add_argument("-e", "--end", help="End", type=int)
    args = parser.parse_args()
 
    start = args.start
    end = args.end
    length = end - start

    # Parse the fasta
    for seq_record in SeqIO.parse(args.input, "fasta"):
        seq = seq_record.seq
        if len(seq) >= length:
            print(seq[start:end])
        else:
            print(seq)

    # done
    print("Done")


if __name__ == "__main__":
    main()
