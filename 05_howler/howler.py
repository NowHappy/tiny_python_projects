#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-10-02
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=argparse.FileType('wt'),
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_args = args.input
    outfile_args = args.outfile

    if os.path.isfile(args.input):
        str_args = open(str_args).read()

    print(f'{str_args.upper()}', file=outfile_args) if outfile_args else print(f'{str_args.upper()}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
