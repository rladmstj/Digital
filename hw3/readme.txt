- 한국어 형태소 분석에 대한 실습을 한다.

- 본인에게 배정된 파일에 형태소 분석 결과를 작성하여 제출해야 함 (파일 배정은 아래에 있음)

- sample 파일의 형식은 각 줄(line)에 하나의 어절이 있음
빈(empty) 줄은 문장 경계를 의미함
각 sample 파일은 약 655라인으로 구성됨

- 학습용 말뭉치 : trn.txt
학습용 말뭉치를 참고하여 수작업으로 형태소 분석을 하거나, 프로그래밍을 이용하여 자동/반자동으로 형태소 분석을 해도 무방함

- konlpy (https://konlpy.org/ko/latest/) 설치
$ pip3 install konlpy
또는
$ pip3 install konlpy --break-system-packages

- java 설치
sudo apt update
sudo apt upgrade
sudo apt install default-jdk

- 형식 오류 점검
http://corpus.korea.ac.kr/errorcheck/

위 사이트에 형태소 분석 파일의 내용을 붙여 넣은 후 오류를 확인
오류가 없도록 파일을 수정하여 제출해야 함

- 오류 유형 확인
http://corpus.korea.ac.kr/errorcheck/error_type.html

- 품사 집합
SJ-RIKS 품사 집합을 사용해야 함
http://corpus.korea.ac.kr/tagset.html

- 형태소 분석 파일의 형식은 각 줄에 "어절\t형태소분석결과"이어야 함 (trn.txt와 같은 형식)

- 주의 사항
(정답과 비교를 위해) 파일의 줄을 유지해야 함 (빈 줄도 그대로 유지해야 함)
제출 전 반드시 형식 오류 점검을 할 것!
어떤 방법으로 형태소 분석을 했는지 간단하게 적을 것.

- 학생별 파일 배정

학번    파일 
202    sample07.txt


- 제출물 : 본인의 sample??.txt