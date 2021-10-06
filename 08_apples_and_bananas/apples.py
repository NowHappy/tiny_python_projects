#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-10-06
Purpose: Apples and bananas
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        choices=list('aeiou'),
                        type=str,
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel

    # dictionary = { 'a' : vowel, 'e' : vowel, 'i': vowel, 'o': vowel, 'u': vowel, 'A' : vowel.upper(), 'E': vowel.upper(), 'I': vowel.upper(), 'O': vowel.upper(), 'U': vowel.upper() }

    trans = str.maketrans('aeiouAEIOU',  vowel * 5 + vowel.upper() * 5) # == str.maketrans(dictionary)

    if os.path.isfile(args.text):
        fh = open(args.text, 'rt')
        for line in fh:
            print(f'{line.rstrip().translate(trans)}')
    else:
        print(f'{args.text.translate(trans)}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
