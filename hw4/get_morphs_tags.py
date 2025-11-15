#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

###############################################################################
def get_morphs_tags(tagged):

    result = []
























    return result

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( f"[Usage] {sys.argv[0]} in-file", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1], encoding='utf-8') as fin:

        for line in fin:

            # 2 column format
            segments = line.split('\t')

            if len(segments) < 2:
                continue

            # result : list of tuples
            result = get_morphs_tags(segments[1].rstrip())

            for morph, tag in result:
                print(morph, tag, sep='\t')
