# from konlpy.tag import Komoran

# tagger = Komoran()

# # Komoran → SJ-RIKS 변환 표
# pos_map = {
#     # (1) 체언
#     "NNG": "NNG", "NNP": "NNP", "NNB": "NNB",
#     "NP": "NP", "NR": "NR", "XR": "NNG",   # ← XR을 NNG로 통일
#     # (2) 용언
#     "VV": "VV", "VA": "VA", "VX": "VX",
#     # (3) 수식언
#     "VCP": "VCP", "VCN": "VCP",
#     "MM": "MM", "MAG": "MAG", "MAJ": "MAJ",
#     # (4) 독립언
#     "IC": "IC",
#     # (5) 관계언 (조사)
#     "JKS": "JKS", "JKC": "JKS", "JKG": "JKG", "JKO": "JKO",
#     "JKB": "JKB", "JC": "JKB", "JKV": "JKV", "JKQ": "JKQ", "JX": "JX",
#     # (6) 어미
#     "EP": "EP", "EF": "EM", "EC": "EM",
#     # (7) 의존형태
#     "ETN": "ETN", "ETM": "ETM",
#     "XPN": "XPN", "XSN": "XSN", "XSV": "XSV", "XSA": "XSA",
#     # (8) 기호 및 기타
#     "SF": "SF", "SP": "SP", "SS": "SS", "SE": "SE", "SO": "SO",
#     "SL": "SL", "SH": "SH", "SW": "SW",
#     "SN": "SN", "NA": "NA"
# }

# text = '''
# ‘희망나눔학교’
# 프로그램을
# 진행해
# 왔다.

# ‘매달
# ○○만
# 원씩
# 36개월만
# 내면
# 신차가
# 내
# 품에….’
# '''

# lines = text.splitlines()

# for line in lines:
#     if line.strip():  # 내용이 있는 줄
#         morphs = tagger.pos(line)
#         # 품사를 SJ-RIKS 기준으로 변환 (XR→NNG 포함)
#         mapped = [f"{m}/{pos_map.get(p, p)}" for m, p in morphs]
#         print(f"{line}\t{'+'.join(mapped)}")
#     else:
#         print(line)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from konlpy.tag import Komoran

tagger = Komoran()

pos_map = {
    "NNG": "NNG", "NNP": "NNP", "NNB": "NNB",
    "NP": "NP", "NR": "NR", "XR": "NNG",
    "VV": "VV", "VA": "VA", "VX": "VX",
    "VCP": "VCP", "VCN": "VCP",
    "MM": "MM", "MAG": "MAG", "MAJ": "MAJ",
    "IC": "IC",
    "JKS": "JKS", "JKC": "JKS", "JKG": "JKG", "JKO": "JKO",
    "JKB": "JKB", "JC": "JKB", "JKV": "JKV", "JKQ": "JKQ", "JX": "JX",
    "EP": "EP", "EF": "EM", "EC": "EM",
    "ETN": "ETN", "ETM": "ETM",
    "XPN": "XPN", "XSN": "XSN", "XSV": "XSV", "XSA": "XSA",
    "SF": "SF", "SP": "SP", "SS": "SS", "SE": "SE", "SO": "SO",
    "SL": "SL", "SH": "SH", "SW": "SW",
    "SN": "SN", "NA": "NA"
}

def help(arg):
    print(f"\n{arg} Option file(s)", file=sys.stderr)
    print("\n[Option]", file=sys.stderr)
    print("\t-h1: hangeul", file=sys.stderr)
    print("\t-h2: hangeul(hanja)", file=sys.stderr)

def analyze_line(line):
    morphs = tagger.pos(line)
    mapped = [f"{m}/{pos_map.get(p, p)}" for m, p in morphs]
    return '+'.join(mapped)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # stdin에서 읽는 버전 (필요 없으면 지워도 됨)
        for raw in sys.stdin:
            line = raw.rstrip('\n')
            if line.strip():
                print(line, analyze_line(line), sep='\t')
            else:
                print()
        sys.exit(0)

    # 파일 입력 버전
    for filename in sys.argv[1:]:
        with open(filename, 'r', encoding='utf-8') as infp:
            for raw in infp:
                line = raw.rstrip('\n')
                if line.strip():
                    print(line, analyze_line(line), sep='\t')
                else:
                    print()
