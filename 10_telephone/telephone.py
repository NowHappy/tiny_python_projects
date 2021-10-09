#!/usr/bin/env python3
"""
Author : NowHappy <rlfmalehd@gmail.com>
Date   : 2021-10-09
Purpose: Telephone
"""

import argparse
import random
import os
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text of file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if args.mutations > 1 or args.mutations < 0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    mutations = args.mutations
    random.seed(args.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    new_text_line = []
    if os.path.isfile(text):
        print('You said: ', end='')
        for line in open(text, 'rt'):
            new_text_line = list(line.rstrip())
            print(f'"{line.rstrip()}"')
            len_text = len(line.rstrip())
            num_mutations = round(len_text * mutations)
            for i in random.sample(range(len_text), num_mutations):
                # print(f'i = {i}, char = {line[i]}, index = {alpha.find(line[i])}')
                # list.index 함수로 색인 위치 찾으면 없을때 error 발생. 있는지 확인하고 쓰던가 아니면 find 함수 쓸 것!!
                # find 반환값 : 색인 위치. 찾을 수 없는 경우 -1 반환
                new_text_line[i] = random.choice(alpha.replace(line[i], '')) # replace 함수는 line[i] 에 해당하는 문자가 alpha에 '있으면' 해당 문자를 치환한다. 없어도 error 안 남.
        print(f'I heard : "' + ''.join(new_text_line)+ '"')
    else:
        print(f'You said: "{text}"')
        new_text_line = list(text)
        len_text = len(text)
        num_mutations = round(len_text * mutations)
        for i in random.sample(range(len_text), num_mutations):
            new_text_line[i] = random.choice(alpha.replace(text[i], ''))
        print(f'I heard : "' + ''.join(new_text_line)+ '"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
