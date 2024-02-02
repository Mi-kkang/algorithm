di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


t = int(input())        # 테스트 케이스 개수 입력받기
for tc in range(1, t+1) :
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0       # 최대 꽃가루 합계

    for i in range(n) :     # n x m 크기의 게임판
        for j in range(m) :
            cnt = arr[i][j]     # 터트린 풍선의 꽃가루 수
            # 주변 풍선의 꽃가루
            for k in range(4) : # 주변 풍선의 인덱스 ni, nj
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m :
                    cnt += arr[ni][nj]
            # 꽃가루를 최대값과 비교
            if max_v < cnt :
                max_v = cnt

    print(f'#{tc} {max_v}')