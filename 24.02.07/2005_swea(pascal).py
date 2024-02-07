t = int(input())            # 테스트 케이스 받기

for tc in range(1, t+1) :
    n = int(input())        # 파스칼의 삼각형의 줄 길이에 넣을 n
    arr = [[0]*n for _ in range(n)]

    for j in range(n) :     # 1이 확정적으로 들어가는 구간에 1넣깅
        arr[j][0] = 1
        arr[j][j] = 1

    for i in range(2, n) :
        for j in range(1, n) :
            if arr[i][j] == 1 :     # 만약 이미 1이 채워져있는 칸을 만나면
                break               # 탈추울~!!
            else :
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]     # 아니면... 위에 두개 더해서 값으로 쓰기!

    print(f'#{tc}')
    for k in range(n) :
        for l in range(k+1) :
            print(arr[k][l], end=' ')

        print()