#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

###############################################################################


def word_count(filename):

    word_freq = defaultdict(int)

    with open(filename, "r", encoding='utf-8') as fin:

        for word in fin.read().split():
            word_freq[word] += 1

    return word_freq


###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()
    input_files = sys.argv[1:]
    n_files = len(input_files)

    # 단어: [파일1빈도, 파일2빈도, ...] 형태
    totalYearCount = defaultdict(lambda: [0] * n_files)

    for idx, input_file in enumerate(input_files):
        word_freq = word_count(input_file)

        for w, freq in word_freq.items():
            totalYearCount[w][idx] = freq   # 해당 파일 위치에만 값 채우기

    with open("result.txt", "w", encoding="utf-8") as fout:
        for w, freq in sorted(totalYearCount.items()):
            print(f"{w}\t{freq}", file=fout)
