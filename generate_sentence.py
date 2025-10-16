#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle  # load
import random  # choice, choices
import sys
import math  # log

################################################################################
# 빈도를 가중치로 적용하여 다음 단어 선택 (random.choices 사용)
# 현재 단어가 모델에 없는 경우, 유니그램에서 랜덤하게 단어 선택


def get_next_word(model, current_word):
    unigram_counts = model['unigram_counts']
    bigram_counts = model['bigram_counts']

    # current_word가 bigram에 없는 경우
    if current_word not in bigram_counts:
        words = list(unigram_counts.keys())
        weights = list(unigram_counts.values())
        return random.choices(words, weights=weights, k=1)[0]

    # bigram에서 다음 단어 후보와 가중치 불러오기
    next_words = list(bigram_counts[current_word].keys())
    weights = list(bigram_counts[current_word].values())
# bigranm_counts[current_word] 가 딕셔너리임
    # 가중치 기반 랜덤 선택
    return random.choices(next_words, weights=weights, k=1)[0]

################################################################################
# 문장의 로그 확률 계산 (로그 취한 개별 확률들의 합)
# 모델에 없는 단어 또는 단어 바이그램이 있으면 -100을 더함


def get_probability(model, sentence):
    # 로그 확률 초기화
    log_prob = 0.0
    unigram_counts = model['unigram_counts']
    bigram_counts = model['bigram_counts']

    # 문장 토큰화 및 <s>, </s> 추가
    words = ["<s>"] + sentence.split() + ["</s>"]

    for i in range(1, len(words)):
        prev = words[i - 1]
        curr = words[i]

        # bigram이나 unigram이 없으면 패널티(-100)
        if prev not in bigram_counts or curr not in bigram_counts[prev]:
            log_prob += -100
            continue

        # 조건부 확률 P(curr | prev)
        bigram_count = bigram_counts[prev][curr]
        unigram_count = unigram_counts[prev]
        prob = bigram_count / unigram_count

        log_prob += math.log(prob)

    return log_prob

################################################################################
# 랜덤 문장 생성
# start_with : 생성할 문장의 시작 단어(들). 없으면 '<s>'로 초기화


def generate_sentence(model, start_with):
    sentence = []

    # 시작 단어 설정
    if not start_with.strip():
        current_word = "<s>"
    else:
        words = start_with.split()
        current_word = words[-1]  # 입력된 마지막 단어로부터 시작
        sentence.extend(words)    # 이미 입력된 단어들 포함

    # 다음 단어를 반복적으로 생성
    while True:
        next_word = get_next_word(model, current_word)
        if next_word == "</s>":
            break
        sentence.append(next_word)
        current_word = next_word

    return ' '.join(sentence)

################################################################################


def load_model(model_file):
    with open(model_file, 'rb') as f:
        return pickle.load(f)

################################################################################


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} model_file")
        sys.exit(1)

    model_file = sys.argv[1]
    model = load_model(model_file)

    print("2-gram 언어 모델 문장 생성기")

    while True:
        cmd = input("\n엔터 또는 문장 시작 단어(들) (q=종료): ")

        if cmd.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        else:
            print("\n<<<< 생성된 문장 >>>>")

            for i in range(10):
                sentence = generate_sentence(model, cmd)
                log_prob = get_probability(model, sentence)
                print(f"문장{i+1} : {sentence} (로그 확률: {log_prob:.4f})")


################################################################################
if __name__ == "__main__":
    main()
