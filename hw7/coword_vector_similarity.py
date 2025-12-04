#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pickle
import math  # sqrt

###############################################################################


def cosine_similarity(t_vector, c_vector):
    common_keys = set(t_vector.keys()) & set(c_vector.keys())
    if not common_keys:
        return 0.0  # 공통 차원이 없으면 유사도 0
    dot_product = sum(t_vector[k] * c_vector[k] for k in common_keys)
    t_magnitude = math.sqrt(sum(v ** 2 for v in t_vector.values()))

    c_magnitude = math.sqrt(sum(v ** 2 for v in c_vector.values()))
    if t_magnitude == 0 or c_magnitude == 0:
        return 0.0  # 벡터의 크기가 0이면 유사도 0
    return dot_product / (t_magnitude * c_magnitude)


###############################################################################
def most_similar_words(word_vectors, target, topN=10):

    result = {}
    # 타겟의 공기어들과 공기어들의 공기어들을 리스트로 저장하기(ㅡㅌ) 그다음에 타겟과 리스트 각항목간의 유사도를 계산한 후 각항목:유사도 로 딕셔너리에 저장
    words = set()
    for x in word_vectors[target].keys():
        if x in word_vectors:

            words.add(x)
            for y in word_vectors[x].keys():

                words.add(y)

    for word in words:
        if word == target:
            continue

        if word in target:
            continue
        sim = cosine_similarity(word_vectors[target], word_vectors[word])
        if sim > 0.001:
            result[word] = sim

    return sorted(result.items(), key=lambda x: x[1], reverse=True)[:topN]

###############################################################################


def print_words(words):
    for word, score in words:
        print("%s\t%.3f" % (word, score))


###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("[Usage]", sys.argv[0], "in-file(pickle)", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1], "rb") as fin:
        word_vectors = pickle.load(fin)

    while True:

        print('\n검색할 단어를 입력하세요(type "^D" to exit): ', file=sys.stderr)

        try:
            query = input()

        except EOFError:
            print('프로그램을 종료합니다.', file=sys.stderr)
            break

        # result : list of tuples, sorted by cosine similarity
        result = most_similar_words(word_vectors, query, topN=30)

        if result:
            print_words(result)
        else:
            print('\n결과가 없습니다.')
