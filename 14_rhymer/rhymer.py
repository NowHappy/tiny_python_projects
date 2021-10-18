#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-10-15
Purpose: Make rhyming "words"
"""

import argparse
import re
import string as s

consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou'])


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    first, second = stemmer(args.word)

    ex = [c for c in s.ascii_lowercase if c not in 'aeiou']
    ex.extend(['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st',
          'sw', 'th', 'tr', 'tw', 'thw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr'])
    ex.sort()

    if second:
        if len(first) != 0:
            ex.remove(first)
        for c in ex:
            print(f'{c}{second}')
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""
    match = re.match(f'([{consonants}]+)?([aeiou])(.*)', word.lower())
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return p1, p2 + p3
    else:
        return word.lower(), ''


# --------------------------------------------------
def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
