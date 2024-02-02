t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    page, Ap, Bp = map(int, input().split())    # 전체 페이지 수, A, B가 찾을 쪽 번호 입력

    a_try, b_try = 0, 0     # A와 B가 이진탐색을 시도한 회수를 저장할 변수 저장함

    start_a = 1       # 맨 처음 페이지 수
    start_b = 1
    page_A = page
    page_B = page

    while start_a <= page_A :
        middle = int((start_a + page_A) / 2)
        a_try += 1
        if middle == Ap :
            break
        elif middle > Ap :
            page_A = middle

        else :
            start_a = middle

    while start_b <= page_B:
        middle = int((start_b + page_B) / 2)
        b_try += 1
        if middle == Bp:
            break
        elif middle > Bp:
            page_B = middle

        else:
            start_b = middle

    if a_try < b_try :
        print(f'#{tc} A')

    elif a_try > b_try :
        print(f'#{tc} B')

    else :
        print(f'#{tc} 0')