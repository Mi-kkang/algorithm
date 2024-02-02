import sys
sys.stdin = open('input_ladder.txt','r')

t = 10      # 총 10개의 테스트 케이스가 주어진다.

for tc in range(1, t+1) :
    test_num = int(input())   # 테스트 케이스의 번호를 입력받기
    n = 100                   # 2차원 배열의 행, 열 크기 (100 x 100)
    arr = [list(map(int, input().split())) for _ in range(n)]   # n x n 사다리 배열 만들기

    end_ro = 0
    end_co = 0      # 원하는 사다리 맨 아래쪽의 행, 열을 저장할 변수 생성

    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 2 :
                end_ro = i
                end_co = j

    while end_ro > 0 :
        if end_co == 0 :
            if arr[end_ro][end_co+1] == 1 :
                end_co += 1
                while arr[end_ro][end_co] == 1 :
                    end_co += 1
                end_co -= 1
                end_ro -= 1
            else :
                end_ro -= 1

        elif end_co == n-1 :
            if arr[end_ro][end_co-1] == 1 :
                end_co -= 1
                while arr[end_ro][end_co] == 1 :
                    end_co -= 1
                end_co += 1
                end_ro -= 1
            else :
                end_ro -= 1

        else :
            if arr[end_ro][end_co+1] == 1 :
                end_co += 1
                if end_co == n-1 :
                    end_ro -= 1
                    continue
                else :
                    while arr[end_ro][end_co] == 1 :
                        if end_co == n-1 :
                            end_ro -= 1
                            continue
                        else:
                            end_co += 1
                    end_co -= 1
                    end_ro -= 1

            elif arr[end_ro][end_co-1] == 1 :
                end_co -= 1
                if end_co == 0 :
                    end_ro -= 1
                    continue
                else :
                    while arr[end_ro][end_co] == 1 :
                        if end_co == 0 :
                            end_ro -= 1
                            continue
                        else:
                            end_co -= 1
                    end_co += 1
                    end_ro -= 1

            else :
                end_ro -= 1

    print(f'#{tc} {end_co}')