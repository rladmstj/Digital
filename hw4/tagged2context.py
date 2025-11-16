#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import get_morphs_tags as mf

###############################################################################
# 명사, 복합명사 추출


def get_index_terms(mt_list):
    INDEX_POS = {"NNG", "NNP", "NNB", "NR", "SL", "SH", "SN"}
    SINGLE_POS = {"NNG", "NNP", "SH", "SL"}

    nouns = []
    n = len(mt_list)

    # 1) 복합어 구간 저장
    compounds = {}  # {end_index: (start, end, compound)}
    i = 0
    while i < n:
        m, t = mt_list[i]
        if t not in INDEX_POS:
            i += 1
            continue

        j = i
        while j < n and mt_list[j][1] in INDEX_POS:
            j += 1

        if (j - i) >= 2:
            comp = "".join([mm for mm, tt in mt_list[i:j]])
            compounds[j - 1] = (i, j - 1, comp)

        i = j

    # 2) 복합어 내부 SL 위치만 삭제
    remove_sl_positions = set()
    for end_idx, (start, end, comp) in compounds.items():
        for pos in range(start, end + 1):
            morph, tag = mt_list[pos]
            if tag == "SL":
                remove_sl_positions.add(pos)

    # 3) 단일어 + 복합어 출력
    for idx, (m, t) in enumerate(mt_list):

        # 단일어 출력
        if t in SINGLE_POS:
            if not (t == "SL" and idx in remove_sl_positions):
                nouns.append(m)

        # 복합어 출력 (end index에서만)
        if idx in compounds:
            nouns.append(compounds[idx][2])

    return nouns


###############################################################################
# Converting POS tagged corpus to a context file


def tagged2context(input_file, output_file):

    with open(input_file, "r", encoding='utf-8') as fin, open(output_file, "w", encoding='utf-8') as fout:

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
        print(f"[Usage] {sys.argv[0]} file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:
        output_file = input_file + ".context"

        print(f"processing {input_file} -> {output_file}", file=sys.stderr)

        # 형태소 분석 파일 -> 문맥 파일
        tagged2context(input_file, output_file)
