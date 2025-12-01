#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
from itertools import combinations

###############################################################################


def print_word_freq(filename, word_freq):
    with open(filename, "w", encoding="utf-8") as filename:
        for w, freq in sorted(word_freq.items()):
            print(f"{w}\t{freq}", file=filename)

###############################################################################


def print_coword_freq(filename, coword_freq):
    with open(filename, "w", encoding="utf-8") as filename:
        for w, freq in sorted(coword_freq.items()):
            print(f"{w[0]}\t{w[1]}\t{freq}", file=filename)

    ###############################################################################


def get_coword_freq(filename):

    coword_freq = defaultdict(int)
    word_context_size = defaultdict(int)
    word_freq = defaultdict(int)
    total_unigram_count = 0

    with open(filename, "r", encoding='utf-8') as fin:

        for line in fin:
            words = line.strip().split()
            unique_words = set(words)

            # unigram 빈도 계산
            for w in unique_words:
                word_freq[w] += 1
                word_context_size[w] += len(unique_words)
                total_unigram_count += 1
            word_freq["#Total"] = total_unigram_count
            # co-word (bigram) 빈도 계산
            for w1, w2 in combinations(sorted(unique_words), 2):
                if ((w2, w1) in coword_freq):
                    continue
                else:
                    coword_freq[(w1, w2)] += 1

    return word_freq, coword_freq, word_context_size


###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:

        print(f"processing {input_file}", file=sys.stderr)

        file_stem = input_file
        pos = input_file.find(".")
        if pos != -1:
            file_stem = input_file[:pos]  # ex) "2017.tag.context" -> "2017"

        # 1gram, 2gram, 1gram context 빈도를 알아냄
        word_freq, coword_freq, word_context_size = get_coword_freq(input_file)

        # unigram 출력
        print_word_freq(file_stem+".1gram", word_freq)

        # bigram(co-word) 출력
        print_coword_freq(file_stem+".2gram", coword_freq)

        # unigram context 출력
        print_word_freq(file_stem+".1gram_context", word_context_size)
