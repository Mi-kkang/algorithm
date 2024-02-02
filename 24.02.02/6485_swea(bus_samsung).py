t = int(input())            # 테스트 케이스의 개수

for tc in range(1, t+1) :
    n = int(input())        # 노선의 개수
    counts = [0] * 5001     # 버스 노선 번호를 카운트 하기 위해 만든 리스트

    for i in range(n) :
        A, B = map(int, input().split())    # 시작 정류장, 끝 정류장 입력 받기

        for j in range(A, B+1) :
            counts[j] += 1

    p = int(input())        # 버스 정류장의 개수를 받아온다.

    bus_stop = [int(input()) for _ in range(p)]

    print(f'#{tc}', end=' ')
    for k in bus_stop :
        print(counts[k], end=' ')

    print()