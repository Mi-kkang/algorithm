T = int(input())    # 테스트 케이스 받기
for tc in range(1, T+1) :
    N = int(input())    # 테스트 케이스 첫 줄에 칠할 영역의 개수 N 받기
    area_arr = [[0]*10 for _ in range(10)]  # 기본 격자 칸 만들기
    # 왼쪽 위 모서리 인덱스 r1,c1, 오른쪽 아래 모서리 r2,c2 와 색상정보 color 2차원 배열로 받기 (1이 빨강 2가 파랑)
    color_arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0   # 겹치는 부분 카운팅

    for co in color_arr :
        r1, c1 = co[0], co[1]
        r2, c2 = co[2], co[3]
        color = co[4]

        for i in range(r1, r2+1) :
            for j in range(c1, c2+1) :

                if area_arr[i][j] == 0 :   # 아무것도 저장되어 있지 않을 때 색을 저장한다.
                    area_arr[i][j] = color

                elif area_arr[i][j] == color :  # 지금 있는 컬러 값과 같은 값이 저장되어있을 때 건너뛰기
                    continue

                else :
                    area_arr[i][j] = color  # 다른 값이 저장되어있을 때 색 다시 저장하고, 플러스 1 하기
                    count += 1

    print(f'#{tc} {count}')