t = int(input())  # 테스트 케이스 개수 받기

for tc in range(1, t + 1):
    word = input()          # 단어 받기
    cnt = len(word)
    # wo_li = list(word)      # 받은 단어를 리스트로 저장하기
    idx = 0                 # 리스트 인덱스를 계산하기 위한 변수 설정
    nu = 0
    n = True

    while n :
        if cnt > 1 :
            for i in range(cnt-1) :
                if word[i] == word[i+1] :
                    word = word[:i] + word[i+2:]

                if cnt != len(word) :
                    break
            cnt = len(word)

            if word == set(word) :
                n = False

        else :
            n = False

    print(f'#{tc} {len(word)}')


    # for i in range(cnt) :
    #     wor_li.append(word[nu])
    #     if idx == 0 :
    #         idx += 1
    #         nu += 1
    #
    #     else :
    #         if wor_li[idx] == wor_li[idx-1] :
    #             del wor_li[idx]
    #             del wor_li[idx-1]
    #             idx -= 2
    #             nu += 1
    #
    #
    # print(wor_li)