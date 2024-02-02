t = int(input())        # 테스트 케이스 개수를 받아온다

for tc in range(1, t+1) :
    n, m = map(int, input().split())        # 배열을 만들 n 과 파리채를 만들 m을 받는다
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 파리가 있는 n x n 배열을 만든다 / 거기에 행, 열이 모두 0인 칸도 하나씩 추가해준다. ==> 따라서 (n+1) x (n+1) 배열이다.
    n += 1  # 배열의 개수가 하나 증가했으니 n 의 값도 하나 증가시켜 준다.

    max_df = 0      # 가장 많은 파리가 죽은 수를 저장할 변수 설정 / 0으로 초기화 해준다.

    for i in range(n-m) :
        for j in range(n-m) :
            dead_f = 0      # 죽은 파리의 개수를 셀 변수 설정

            for k in range(m) :     # 파리채 크기만큼 파리를 잡아봅시다!
                for l in range(m) :
                    dead_f += arr[i+k][j+l]

            if max_df <= dead_f :   # 잡은 파리와 제일 많이 잡은 파리의 수를 비교해서 더 크면 새로 저장해줌!
                max_df = dead_f

    print(f'#{tc} {max_df}')