#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-09-30
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        nargs='+',
                        metavar='str', # for help
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    if num < 2:
        print(f'You are bringing {items[0]}.')
    elif num < 3:
        print(f'You are bringing {items[0]} and {items[1]}.')
    else:
        items[-1] = 'and ' + items[-1]
        print('You are bringing ' + ', '.join(items) + '.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
