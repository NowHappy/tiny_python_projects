#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-10-04
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    t_num_lines = t_num_words = t_num_bytes = 0

    for fh in args.file:
        num_lines = num_words = num_bytes = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')
        t_num_lines += num_lines
        t_num_words += num_words
        t_num_bytes += num_bytes

    if len(args.file) > 1:
        print(f'{t_num_lines:8}{t_num_words:8}{t_num_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
