#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-10-13
Purpose: Ransom Note
"""

import argparse
import random
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    if os.path.isfile(args.text):
        for line in open(args.text, 'rt'):
            print(''.join(map(choose, line.rstrip())))
    else:
        print(''.join(map(choose, args.text)))


# --------------------------------------------------
def choose(char):
    """change a character"""

    # return char.upper() if random.choice([False, True]) else char.lower()
    return random.choice([char.lower(), char.upper()])


# --------------------------------------------------
def test_choose():
    """test choose"""
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
