def printList(dic) :
    for key in dic.keys() :
        print('{:15} : {}'.format(key,dic[key]))

## 파일->딕셔너리
# 파일에서 읽어오기
file = 's:\python\dictionary.txt'
f = open(file,'r',encoding='UTF8')
if f.readable() :
    dic = {}
    for item in f.readlines() :  #파일에서 한줄을 읽어 문자열로 가져옮  blackboard      :칠판\n
        list = item.split(':')   #문자열을 ':'를 구분자로 배열로 반환
        dic[list[0].strip()]=list[1][:-1] #문자열 슬라이싱
    f.close()

print('>> 영어 단어장 << ')
stop = False
while not stop :
    print('메뉴 >> 1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료')
    choice = int(input('선택 >> '))

    if choice == 1 :    #저장
        if len(dic) >= 5:
            print("최대 5개만 저장 가능")
        else:
            print('저장')
            word = input('단어 입력> ')
            meaning = input('뜻 입력 > ')
            if word in dic.keys():
                print('이미 등록된 단어')
            else:
                dic[word] = meaning
    elif choice == 2:   #검색
        word = input('검색할 단어를 입력하세요: ').lower()
        result = []
        for key in dic.keys():
            if key.startswith(word):
                result.append((key, dic[key]))
        if len(result) == 0:
            print('단어를 검색할 수 없습니다.')
        else:
            printList(dict(result))
    elif choice == 3:   #수정
         word = input('수정할 단어를 입력하세요: ').lower()
         if word in dic.keys():
            new_meaning = input(f"{word}의 새로운 뜻을 입력하세요: ")
            dic[word] = new_meaning
            print('단어 뜻 수정했음')
         else:
            print('단어를 검색할 수 없습니다.')
    elif choice == 4:   #삭제
        word = input('삭제할 단어를 입력하세요: ').lower()
        if word in dic.keys():
            del dic[word]
            print('단어를 삭제했습니다.')
        else:
            print('단어를 검색할 수 없습니다.')
    elif choice == 5:   #목록
        print('1. 오름차순 정렬')
        print('2. 내림차순 정렬')
        sub_choice = int(input('정렬 방법을 선택하세요: '))
        sorted_dic = sorted(dic.items())
        if sub_choice == 1:
            for key, value in sorted_dic:
                print(f"{key}: {value}")
        elif sub_choice == 2:
            for key, value in reversed(sorted_dic):
                print(f"{key}: {value}")
        else:
            print('잘못된 선택입니다.')       
    elif choice == 6:   #통계
         # 저장된 단어 갯수
        print(f"저장된 단어 갯수: {len(dic)}")

        # 단어의 문자수가 가장 많은 단어
        longest_word = max(dic, key=lambda x: len(x))
        print(f"단어의 문자수가 가장 많은 단어: {longest_word}")

        # 단어 글자내림차순 출력(단어만)
        print("단어글자내림차순 출력(단어만):")
        for word in sorted(dic.keys(), key=lambda x: x.lower(), reverse=True):
            print(word)

        # 단어 글자수 오름차순으로 출력 (단어만)
        print("단어 글자수 오름차순으로 출력 (단어만):")
        for word in sorted(dic.keys(), key=lambda x: len(x)):
            print(word)
    elif choice == 7:   #종료
        stop = True
        ## 딕셔너리->파일
        # 파일에 저장하기
        if f.writable() :
            for item in dic :
                f.write('{}:{}\n'.format(item[0].strip(), item[1].strip()))
            f.close()
    else :
        print('선택한 메뉴가 없음')
