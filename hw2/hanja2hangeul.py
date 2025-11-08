#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import maxmatch

def help(arg):
    print(f"\n{arg} Option file(s)", file=sys.stderr)
    print("\n[Option]", file=sys.stderr)
    print("\t-h1: hangeul", file=sys.stderr)
    print("\t-h2: hangeul(hanja)", file=sys.stderr)

###############################################################################
# 한자-한글 변환 (문자열 단위; 한자 외 다른 문자들이 포함될 수 있음)
# return value: 한자-한글 변환된 문자열 (형식 1)
# ex) 聖經에 -> 성경에
def hanja2hangeul_str1(str):
    return maxmatch.maxmatch(str)
    
###############################################################################
# 한자-한글 변환 (문자열 단위; 한자 외 다른 문자들이 포함될 수 있음)
# return value: 한자-한글 변환된 문자열 (형식 2)
# ex) 聖經에 -> 성경(聖經)에
def hanja2hangeul_str2(str):
    translated = maxmatch.maxmatch(str, debug=False)
    result = ''
    i = 0
    j = 0

    while i < len(translated) and j < len(str):
        # 두 문자가 같으면 그대로 추가
        if translated[i] == str[j]:
            result += translated[i]
            i += 1
            j += 1
        else:
            # 달라지는 연속 구간 찾기
            diff_t = ''
            diff_s = ''
            start_i = i
            start_j = j

            # translated와 str에서 서로 다른 부분을 끝까지 추적
            while i < len(translated) and j < len(str) and translated[i] != str[j]:
                diff_t += translated[i]
                diff_s += str[j]
                i += 1
                j += 1

            # 괄호로 묶어서 추가
            result += f"{diff_t}({diff_s})"

    # 남은 부분 처리
    if i < len(translated):
        result += translated[i:]
    if j < len(str):
        result += f"({str[j:]})"

    return result
 
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 3:
        help(sys.argv[0])
        sys.exit(1)
        
    if sys.argv[1] == '-h1':
        func = hanja2hangeul_str1

    elif sys.argv[1] == '-h2':
        func = hanja2hangeul_str2

    else:
        help(sys.argv[0])
        sys.exit()
        
    for filename in sys.argv[2:]:

        with open(filename, "r", encoding="utf-8") as infp, open(filename+".out", "w", encoding="utf-8") as outfp:

            print(f"{filename} -> {filename+'.out'}", file=sys.stderr)

            # 파일 읽기 (라인 단위)
            for line in infp:
                result = []
                words = line.split()

                # 각 단어에 대해 한자-한글 변환
                for word in words:
                    result.append(func(word))

                print(' '.join(result), file=outfp)
