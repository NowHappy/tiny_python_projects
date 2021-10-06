#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        help='Letter(s)',
                        nargs='+')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    args = parser.parse_args()

    args.sentences = { line[0].upper() : line.rstrip() for line in args.file }

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for letter in args.letter:
        print(args.sentences.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
