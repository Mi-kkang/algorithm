t = 1      # 총 10개의 테스트 케이스가 주어진다.

for tc in range(1, t+1) :
    test_num = int(input())   # 테스트 케이스의 번호를 입력받기
    n = 100                   # 2차원 배열의 행, 열 크기 (100 x 100)
    arr = [list(map(int, input().split())) for _ in range(n)]   # n x n 사다리 배열 만들기

    start_la = []             # 사다리가 시작할 수 있는 곳을 리스트로 만들기
    for i in range(n) :
        if arr[0][i] == 1 :
            start_la.append(i)


    for ld in range(len(start_la)) :
        m_ro = 0
        m_co = start_la[ld]           # 사다리 시작 행, 열 만들기
        cross_li = []
        cross_li.append(m_co)

        while m_ro <= n-1 :
            if m_co == 0 :
                if arr[m_ro][m_co+1] == 1 :
                    if start_la[ld+1] not in cross_li :
                        m_co += start_la[ld+1] - start_la[ld]
                        cross_li.append(start_la[ld+1])
                    else :
                        m_ro += 1
                else :
                    m_ro += 1

            elif m_co == n-1 :
                if arr[m_ro][m_co-1] == 1 :
                    if start_la[ld-1] not in cross_li :
                        m_co += start_la[ld] - start_la[ld-1]
                        cross_li.append(start_la[ld - 1])
                    else:
                        m_ro += 1
                else :
                    m_ro += 1

            elif 0 < m_co < n-1 :
                if arr[m_ro][m_co+1] == 1 or arr[m_ro][m_co-1] == 1 :
                    if start_la[ld+1] not in cross_li :
                        m_co += start_la[ld+1] - start_la[ld]
                        cross_li.append(start_la[ld + 1])

                    elif start_la[ld-1] not in cross_li :
                        m_co += start_la[ld] - start_la[ld - 1]
                        cross_li.append(start_la[ld - 1])

                    else :
                        m_ro += 1
                else :
                    m_ro += 1






        if m_co == n-1 and m_ro == n-1 :
            print(f'#{tc} {start_la[ld]}')
            break
