- 수업 내용에서 소개한 (한자-한글 변환.pptx 참고) 한자 처리와 관련된 내용 중 한자-한글 변환의 일부 기능을 구현한다.

- 과제 설명 영상을 따라 "부록A_검색엔진용한자음가사전_최종.xls" 엑셀 파일로부터 한자-한글 테이블을 생성하여 hanja2hangeul_table.py로 저장한다.

- 제공된 한자어-한글 사전(hanja2hangeul_dic.py)을 이용하여 최장일치(maxmatch) 알고리즘을 구현한 maxmatch.py를 완성한다.
  
  현재 위치에서 가능한 가장 긴 부분 문자열이 사전에 있는지 검사
  매칭되는 문자열이 없으면 한 글자를 한자-한글 테이블에서 찾아 한글로 변환
    (한글음가의 중의성이 있는 한자의 경우 한자-한글 테이블 상 첫번째 음가로 변환할 것)
  만약 변환할 수 없는 문자는 그대로 둠 (예) 음가가 등록되지 않은 한자 또는 한자가 아닌 문자)

- 한자-한글 변환 프로그램(hanja2hangeul.py)을 완성한다.

- 실행 방법
$ ./hanja2hangeul.py 옵션 입력파일(s) # 출력파일은 각 입력파일.out으로 저장됨

$ ./hanja2hangeul.py -h1 sample.txt   # 한자 -> 한글
$ ./hanja2hangeul.py -h2 sample.txt   # 한자 -> 한글(한자)


- 제출 파일 : hanja2hangeul_table.py, hanja2hangeul_dic.py maxmatch.py hanja2hangeul.py (파일명을 수정하지 말 것! 압축 파일로 만들지 말 것!)

