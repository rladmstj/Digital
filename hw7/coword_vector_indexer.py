#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pickle

###############################################################################


def vector_indexing(filename):
    with open(filename, "r", encoding='utf-8') as fin:
        word_vectors = dict()
        for line in fin:
            words = line.strip().split()

            word = words[0]
            key = words[1]
            value = float(words[2])

            if word not in word_vectors:
                word_vectors[word] = dict()
            word_vectors[word][key] = value
    return word_vectors


###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"[Usage] {sys.argv[0]} in-file out-file(pickle)",
              file=sys.stderr)
        sys.exit()

    filename = sys.argv[1]
    print(f"processing {filename} ...", file=sys.stderr)

    # 공기어 벡터 저장 (dictionary of dictionary)
    word_vectors = vector_indexing(filename)

    print(f"# of entries = {len(word_vectors)}", file=sys.stderr)

    with open(sys.argv[2], "wb") as fout:
        print(f"saving {sys.argv[2]}", file=sys.stderr)
        pickle.dump(word_vectors, fout)
