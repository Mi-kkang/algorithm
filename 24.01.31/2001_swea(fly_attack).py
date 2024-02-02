t = int(input())    # 테스트 케이스 개수를 구한다.

for tc in range(t) :
    N, M = map(int, input().split())    # 배열 크기인 N과 파리채의 크기 M 받기.
    arr = [list(map(int,input().split())) for _ in range(N)]    # N x N 배열 만들기

    max_fly = 0     # 최대 파리 개수 찾기

    for i in range(N-M+1) :
        for j in range(N-M+1) :
            fly_num = 0  # 파리의 개수 구하기
            for k in range(M) :
                for l in range(M) :
                    fly_num += arr[i+k][j+l]    # 범위 안에 있는 파리의 개수 더하기

            # 만약 최대 파리의 개수보다 크면 다시 재할당
            if max_fly <= fly_num :
                max_fly = fly_num


    print(f'#{tc+1} {max_fly}')