t = 10      # 10개의 테스트 케이스가 주어진다.
N = 100     # 배열의 크기 // 100 x 100 으로 동일하다.

for tc in range(t) :
    tc_num = int(input())   # 몇 번째 테스트 케이스인지 알려주는 번호
    arr = [list(map(int, input().split())) for _ in range(N)]   # 수를 받아 배열에 저장한다.

    row_max, column_max = 0, 0      # 행과 열의 최댓값 생성, 0으로 초기화
    fo_cross, ba_cross = 0, 0       # 정방향, 역방향 대각선 길이 넣을 변수 생성
    max_corss = 0                   # 대각선 최댓값 생성, 0으로 초기화
    total_max = 0                   # 총 최댓값을 생성, 0으로 초기화

    for i in range(N) :
        row_sum = 0
        column_sum = 0
        for j in range(N) :
            row_sum += arr[i][j]
            column_sum += arr[j][i]

        if row_max <= row_sum :
            row_max = row_sum

        if column_max <= column_sum :
            column_max = column_sum

    if row_max > column_max :
        total_max = row_max

    else:
        total_max = column_max


    for k in range(N) :
        fo_cross += arr[k][k]
        ba_cross += arr[k][N-1-k]

    if fo_cross > ba_cross :
        max_corss = fo_cross

    else :
        max_corss = ba_cross


    if max_corss > total_max :
        total_max = max_corss


    print(f'#{tc_num} {total_max}')