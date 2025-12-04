1. 대상어와 공기어 쌍들의 t-점수가 저장된 입력파일로부터 단어 벡터(공기어 벡터)를 생성하는 coword_vector_indexer.py를 작성한다. (코퍼스 분석 로드맵.pptx p.28~29 참고)

완성된 스크립트의 실행 방법은 다음과 같다.

$ ./coword_vector_indexer.py 입력파일 출력파일
예) $ ./coword_vector_indexer.py all.tscore all.pickle

* 출력 파일은 dictionary의 dictionary 형식의 pickle 파일임

2. 사용자 질의(query)와 가장 유사한 30개의 단어(관련어)와 유사도를 보여주는 coword_vector_similarity.py를 작성한다. (코퍼스 분석 로드맵.pptx p.30~32 참고)

예) $ ./coword_vector_similarity.py all.pickle

* 입력 파일은 단어 벡터(공기어 벡터)가 pickle 형태로 저장된 파일임

* 제약 사항
- 관련어 후보는 대상어의 공기어들과 공기어들의 공기어들로 한정함
- 코사인 유사도가 0.001보다 큰 경우만 저장
- 관련어 후보가 대상어와 같으면 출력하지 않음
- 관련어 후보가 대상어에 포함되면 출력하지 않음 예) 개인정보/정보 *, 교육부장관/장관 *, 인사청문회/청문회 *

* 유사도의 내림차순으로 상위 30개의 관련어를 출력해야 함

* 첨부파일에 다음의 파일들을 첨부함 (결과 비교용)
  - t-점수 파일 (all.tscore)
  - 벡터 파일 (all.pickle)

* 과제에 대한 설명 영상은 "주차학습->15주차"에 있음

* 제출마감 : 12월 19일(금) 오후 11시 59분

* 제출물 : 소스코드(coword_vector_indexer.py, coword_vector_similarity.py) (파일을 압축하지 말 것, 파일명을 변경하지 말 것!)