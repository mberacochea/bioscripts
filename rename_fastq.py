#!/usr/bin/env python

'''Rename contigs of a FASTA file with incremental count.'''

import argparse


def main():
    '''Execute renaming.'''

    # Parse arguments.
    parser = argparse.ArgumentParser(description='Rename FASTA files.', epilog='Work out those contigs.')
    parser.add_argument('-i', '--input', help='indicate input FASTA file', required=True)
    parser.add_argument('--map', help='map current names with the renames', type=str, default='')
    parser.add_argument('-o', '--output', help='indicate output FASTA file', required=True)
    args = parser.parse_args()

    # Open FASTQ
    fastq_in = open(args.input)

    # Create FASTQ output file.
    fastq_out = open(args.output, 'wb')

    # Start counter.
    count = 1

    # Parse file and write to output.
    print('Parsing %s...' % args.input)

    for name, seq, qual in readfq(fastq_in):
        print(name)
        exit(0)
        
        if name == '@MSQ-M01442:4:000000000:A38DN:1:1101:12091:3230':
            print(count)
        fastq_out.write("@{}\n{}\n+{}\n{}".format(str(count), seq, name, qual))
        count += 1

    # Finish
    fastq_out.close()
    fastq_in.close()
    print('Wrote %d sequences on %s.' % (count, args.output))


def readfq(fp): # this is a generator function
    last = None # this is a buffer keeping the last unprocessed line
    while True: # mimic closure; is it a bad idea?
        if not last: # the first record or a record following a fastq
            for l in fp: # search for the start of the next record
                if l[0] in '>@': # fasta/q header line
                    last = l[:-1] # save this line
                    break
        if not last: break
        name, seqs, last = last[1:].partition(" ")[0], [], None
        for l in fp: # read the sequence
            if l[0] in '@+>':
                last = l[:-1]
                break
            seqs.append(l[:-1])
        if not last or last[0] != '+': # this is a fasta record
            yield name, ''.join(seqs), None # yield a fasta record
            if not last: break
        else: # this is a fastq record
            seq, leng, seqs = ''.join(seqs), 0, []
            for l in fp: # read the quality
                seqs.append(l[:-1])
                leng += len(l) - 1
                if leng >= len(seq): # have read enough quality
                    last = None
                    yield name, seq, ''.join(seqs); # yield a fastq record
                    break
            if last: # reach EOF before reading enough quality
                yield name, seq, None # yield a fasta record instead
                break

if __name__ == '__main__':
    main()

