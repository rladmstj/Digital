연도별 문맥 파일들로부터 연도별 단어 빈도를 추출하는 word_frequency_by_year.py를 작성한다.

스크립트의 실행 방법은 다음과 같다.

$ ./word_frequency_by_year.py 입력파일(s) > 출력파일
예) $ ./word_frequency_by_year.py *.context > result.txt

* 결과 출력 형식은 다음과 같음
단어\t빈도리스트

예) 컴퓨터    [70, 46, 29, 35, 32, 36, 26, 22, 19, 24, 18, 20, 15, 20, 16, 14, 20, 5, 9, 11]

* 단어순으로 정렬하여 출력해야 함

* 첨부파일에 다음의 파일들을 첨부함
  - 연도별 문맥 파일 (2000.tag.context ~ 2019.tag.context)
  - 스크립트에 대한 실행 결과 (result.txt)
  - word_frequency.py

* 과제에 대한 설명 영상은 "주차학습->13주차"에 있음

* 제출마감 : 12월 8일(월) 23:59:00까지

* 제출물 : 소스코드(word_frequency_by_year.py) (파일명을 변경하지 말 것!)