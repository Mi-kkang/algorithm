t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, Q = map(int, input().split())        # 상자의 개수 N, 숫자 바꾸는 작업 횟수 Q 받기
    box_li = [0] * N

    for n in range(Q) :
        L, R = map(int, input().split())    # 숫자를 바꿀 시작 상자와 끝 상자의 값을 받는다.

        # 시작 상자와 끝 상자의 범위만큼 반복문을 돌린다
        # // 여기서 시작 상자에 -1을 한 이유는 리스트의 인덱스는 주어진 숫자보다 하나 작은 수이기 때문이다.
        for i in range(L-1, R) :
            box_li[i] = n+1

    print(f'#{tc}', end=' ')
    for idx in box_li :
        print(idx, end=' ')

    print()