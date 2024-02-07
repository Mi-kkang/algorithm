t = int(input())        # 테스트 개수 받기

for tc in range(1, t+1) :
    word = input()      # 단어 입력 받기
    wo_li = []          # 연속된 단어를 지운 단어를 넣을 리스트 만들기
    i = 1

    # for wo in word :
    #     if wo_li :
    #         if wo_li[-1] == wo :
    #             wo_li.pop()
    #         else :
    #             wo_li.append(wo)
    #     else :
    #         wo_li.append(wo)

    while i < len(word) :
        if word[i] == word[i-1] :
            word = word[:i-1] + word[i+1:]
            i = 1

        else :
            i += 1

    # print(f'#{tc} {len(wo_li)}')

    print(f'#{tc} {len(word)}')