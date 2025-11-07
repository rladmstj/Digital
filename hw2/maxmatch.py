#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import hanja2hangeul_table
import hanja2hangeul_dic

# 한자-한글 테이블
h2h_table = hanja2hangeul_table.hanja2hangeul_table

# 한자어-한글 사전
h2h_dic = hanja2hangeul_dic.hanja2hangeul_dic

# 한자 문자열을 입력받아 한글로 변환하는 최장일치 알고리즘
# text (str): 변환할 한자 문자열
# debug (bool): 디버깅 여부. True이면 디버깅 정보 출력 ('+'로 구분된 문자열 반환)
# Return: 변환된 한글 문자열
def maxmatch(text, debug=False):
        
    if not text:
        return ""

    result = []

    n = len(text)
    pos = 0
    
    # 한자어-한글 사전에서 발견되는 경우 한글 뒤에 덧붙이는 문자열 예) 半島는  반도*+는
    tag = '*' if debug else ''
        























    
    if debug:
        return '+'.join(result)
    return ''.join(result)

################################################################################
def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            result = []
            
            words = line.split()

            for word in words:
                word_result = maxmatch(word, debug=True)
                result.append(word_result)

                print(word, word_result, sep='\t')

################################################################################
if __name__ == "__main__":
    main()

