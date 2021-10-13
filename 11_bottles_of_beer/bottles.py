#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-10-13
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    bottle_str = str(bottle)
    s1 = 's' if bottle > 1 else ''
    s2 = 's' if bottle != 2 else ''
    next_bottle = str(bottle - 1) if bottle > 1 else 'No more'

    return '\n'.join([
        f'{bottle_str} bottle{s1} of beer on the wall,',
        f'{bottle_str} bottle{s1} of beer,',
        'Take one down, pass it around,',
        # f'{str(bottle - 1)} bottle{s2} of beer on the wall!' if bottle > 1 else 'No more bottles of beer on the wall!'
        f'{next_bottle} bottle{s2} of beer on the wall!'
    ])


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join(['2 bottles of beer on the wall,', '2 bottles of beer,',
                                     'Take one down, pass it around,', '1 bottle of beer on the wall!'
                                     ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # for i in range(args.num, 0, -1):
    #     print(verse(i))
    #     print() if i > 1 else None
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
