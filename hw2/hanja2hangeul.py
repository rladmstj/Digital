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
    pos = 0
    
    # 원본과 변환된 문자열을 비교하여 한자 부분만 괄호 처리
    










    
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
