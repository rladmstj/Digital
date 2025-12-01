#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math  # sqrt

###############################################################################


def read_frequency(filename):

    freqs = {}
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                w = parts[0]
                freq = int(parts[1])
                freqs[w] = freq
            elif len(parts) == 3:
                w1 = parts[0]
                w2 = parts[1]
                freq = int(parts[2])
                freqs[(w1, w2)] = freq

    return freqs

###############################################################################


def calc_tscore(filename, unigrams, unigram_context, uni_N, cutoff):

    t_scores = {}

    with open(filename, "r", encoding='utf-8') as fin:
        for line in fin:
            parts = line.strip().split("\t")
            if len(parts) != 3:
                continue
            for i in range(2):
                if (i == 0):
                    w1 = parts[0]
                    w2 = parts[1]
                else:
                    w1 = parts[1]
                    w2 = parts[0]
                co_freq = int(parts[2])

                if co_freq < cutoff or w2 in w1:
                    continue

                freq_w1 = unigrams.get(w1, 0)
                freq_w2 = unigrams.get(w2, 0)

                context_w1 = unigram_context.get(w1, 0)
                context_w2 = unigram_context.get(w2, 0)

                # 기대빈도 계산
                expected_freq = (context_w1 * freq_w2) / uni_N

                # t-점수 계산
                t_score = (co_freq - expected_freq) / math.sqrt(co_freq)
                if t_score <= 0:
                    continue
                t_scores[(w1, w2)] = t_score

    return t_scores

###############################################################################


def print_tscore(filename, t_scores):
    with open(filename, "w", encoding="utf-8") as fout:
        for w, t_score in sorted(t_scores.items()):
            print(f"{w[0]}\t{w[1]}\t{t_score:.3f}", file=fout)


###############################################################################
if __name__ == "__main__":

    CUTOFF = 5  # 공기빈도가 이 값 이상인 경우만 t점수를 계산

    if len(sys.argv) < 2:
        print("[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:

        print(f"processing {input_file}", file=sys.stderr)

        file_stem = input_file
        pos = input_file.find(".")
        if pos != -1:
            file_stem = input_file[:pos]  # ex) "2017.2gram" -> "2017"

        print(f"\tLoading {file_stem}.1gram", file=sys.stderr)
        unigrams = read_frequency(file_stem+".1gram")

        print(f"\tLoading {file_stem}.1gram_context", file=sys.stderr)
        unigram_context = read_frequency(file_stem+".1gram_context")

        uni_N = unigrams['#Total']  # unigram 빈도 합

        # key : (target, coword)
        # value : t-score
        t_scores = calc_tscore(input_file, unigrams,
                               unigram_context, uni_N, CUTOFF)

        print_tscore(file_stem+".tscore", t_scores)
