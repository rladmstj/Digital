#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

###############################################################################


def get_morphs_tags(tagged):

    result = []

    units = tagged.split('+')

    prev_was_empty = False

    for unit in units:
        unit = unit.strip()

        # 빈 단위: 다음 unit 처리에 사용하기 위해 flag만 켜고 continue
        if unit == "":
            prev_was_empty = True
            continue

        # (1) "/TAG" 형태인데 이전 unit이 empty였다면: "+" 의 TAG 로 본다
        if prev_was_empty and unit.startswith('/') and len(unit) > 1:
            morph = "+"
            tag = unit[1:]
            result.append((morph, tag))
            prev_was_empty = False
            continue

        # flag 초기화
        prev_was_empty = False

        # (2) 정상 형태소/품사: 마지막 '/' 기준 분리
        if '/' in unit:
            idx = unit.rfind('/')
            morph = unit[:idx]
            tag = unit[idx+1:]

            # "/TAG" 처럼 형태소가 비어 있는 경우 → 형태소가 "/" 라고 판단
            if morph == "":
                morph = "/"

            result.append((morph, tag))
            continue

        # (3) "/" 없는 일반 형태소
        result.append((unit, ""))

    return result


###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"[Usage] {sys.argv[0]} in-file", file=sys.stderr)
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
