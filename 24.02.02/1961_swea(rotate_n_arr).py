t = int(input())        # 테스트 케이스 개수를 받는다.

for tc in range(1, t+1) :
    n = int(input())    # n x n 행렬의 행과 열 길이를 결정하는 n 받기
    arr = [list(map(int, input().split())) for _ in range(n)]

    ro_90 = []
    ro_180 = []
    ro_270 = []

    # 90도 회전했을 때 숫자들을 str로 저장해서 더해주기 // 출력값 처럼 나오게 하기 위해서
    for i in range(n) :
        ro_90_nu = ''
        for j in range(n-1, -1, -1) :
            ro_90_nu += str(arr[j][i])

        ro_90.append(ro_90_nu)

    # print(arr)

    # 180도 회전했을 때 숫자들을 str로 저장해서 더해주기 // 출력값 처럼 나오게 하기 위해서
    for i in range(n-1, -1, -1) :
        ro_180_nu = ''
        for j in range(n-1, -1, -1) :
            ro_180_nu += str(arr[i][j])

        ro_180.append(ro_180_nu)

    # 270도 회전했을 때 숫자들을 str로 저장해서 더해주기 // 출력값 처럼 나오게 하기 위해서
    for i in range(n-1, -1, -1) :
        ro_270_nu = ''
        for j in range(n) :
            ro_270_nu += str(arr[j][i])

        ro_270.append(ro_270_nu)

    print(f'#{tc}')
    for i in range(n) :
        print(f'{ro_90[i]} {ro_180[i]} {ro_270[i]}')
    # print(ro_90)
    # print(ro_180)
    # print(ro_270)
