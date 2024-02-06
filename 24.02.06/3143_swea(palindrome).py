def check_palin (n, m, arr) :
    for i in range(n) :
        for j in range(n-m+1) :
            count = 0
            for k in range(m//2) :  # 가로로 회문을 검사하는 방법
                if arr[i][j+k] == arr[i][j+m-(k+1)] :
                    count += 1
            if count == m // 2 :
                print(f'#{tc}', end=' ')
                for l in range(m) :
                    print(arr[i][j+l], end='')
                print()
                return

    for j in range(n) :
        for i in range(n-m+1) :
            count = 0
            for p in range(m//2) :  # 세로로 회문을 검사하는 방법
                if arr[i+p][j] == arr[i+m-(p+1)][j] :
                    count += 1
            if count == m // 2 :
                print(f'#{tc}', end=' ')
                for q in range(m) :
                    print(arr[i+q][j], end='')
                print()
                return



t = int(input())        # 테스트 케이스의 개수 받기

for tc in range(1, t+1) :
    n, m = map(int,input().split())     # nxn 배열을 만들 n, 회문의 길이 m 받기
    arr = [list(map(str, input())) for _ in range(n)]   # nxn 배열을 받는다.

    check_palin(n, m, arr)



