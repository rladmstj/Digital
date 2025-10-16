#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pickle # dump
from collections import defaultdict

# 2gram 언어 모델 학습
# unigram 빈도와 bigram 빈도를 리턴
# 문장의 앞뒤에 시작(<s>)과 끝(</s>)을 나타내는 가상의 단어를 포함해야 함
# 단어 토큰은 공백을 기준으로 분리
def learn_bigram_language_model(input_file):
    # 단어 빈도를 저장할 dictionary
    unigram_counts = defaultdict(int)
    bigram_counts = {} # dictionary of dictionary
    



















    
    return unigram_counts, bigram_counts

################################################################################
def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input_file output_file(pickle)")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # 모델 학습
    unigram_counts, bigram_counts = learn_bigram_language_model(input_file)
    
    # 모델 저장
    model = {
        'unigram_counts': unigram_counts,
        'bigram_counts': bigram_counts
    }
    
    with open(output_file, 'wb') as f:
        pickle.dump(model, f)

################################################################################
if __name__ == "__main__":
    main() 