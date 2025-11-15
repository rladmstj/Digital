#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import get_morphs_tags as mf

###############################################################################
# 명사, 복합명사 추출
def get_index_terms( mt_list):
    nouns = []























    return nouns

###############################################################################
# Converting POS tagged corpus to a context file
def tagged2context( input_file, output_file):

    with open( input_file, "r", encoding='utf-8') as fin, open( output_file, "w", encoding='utf-8') as fout:

        for line in fin:

            # 빈 라인 (문장 경계)
            if line[0] == '\n':
                print(file=fout)
                continue

            try:
                ej, tagged = line.split(sep='\t')
            except:
                print(line, file=sys.stderr)
                continue

            # 형태소, 품사 추출
            # result : list of tuples
            result = mf.get_morphs_tags(tagged.rstrip())

            # 색인어 추출
            terms = get_index_terms(result)

            # 색인어 출력
            for term in terms:
                print(term, end=" ", file=fout)

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( f"[Usage] {sys.argv[0]} file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:
        output_file = input_file + ".context"
        print( f"processing {input_file} -> {output_file}", file=sys.stderr)

        # 형태소 분석 파일 -> 문맥 파일
        tagged2context( input_file, output_file)
