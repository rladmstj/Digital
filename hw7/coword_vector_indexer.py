#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pickle

###############################################################################
def vector_indexing(filename):
    














    return word_vectors
    
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"[Usage] {sys.argv[0]} in-file out-file(pickle)", file=sys.stderr)
        sys.exit()

    filename = sys.argv[1]
    print(f"processing {filename} ...", file=sys.stderr)
    
    # 공기어 벡터 저장 (dictionary of dictionary)
    word_vectors = vector_indexing(filename)

    print(f"# of entries = {len(word_vectors)}", file=sys.stderr)

    with open(sys.argv[2],"wb") as fout:
        print(f"saving {sys.argv[2]}", file=sys.stderr)
        pickle.dump(word_vectors, fout)
