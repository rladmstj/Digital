#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "trn.txt"   # 형태소 분석된 파일
output_file = "sample.txt"  # 원문만 저장할 파일

with open(input_file, "r", encoding="utf-8") as inf, open(output_file, "w", encoding="utf-8") as outf:
    for line in inf:
        # 탭으로 구분된 경우
        if '\t' in line:
            original = line.split('\t', 1)[0]
            outf.write(original.strip() + '\n')
        # 빈 줄은 그대로 유지
        elif line.strip() == '':
            outf.write('\n')
        else:
            # 혹시 탭 없는 줄도 그대로 넣기
            outf.write(line.strip() + '\n')

print(f"✅ '{output_file}' 파일에 원문만 복원 완료!")
