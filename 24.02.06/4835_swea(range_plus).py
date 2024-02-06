t = int(input())

for tc in range(1, t+1) :
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # max_v = 0
    # min_v = 1000000
    s = 0               # 구간의 합
    for i in range(M) : # 첫 구간의 합
        s += arr[i]

    min_v = max_v = s

    for i in range(N-M) :       # 이미 계산된 구간의 합에서 제외할 맨 앞 원소
        s -= arr[i]
        s += arr[i+M]       # 현재 구간 다음 원소를 구간에 추가
        if min_v > s :
            min_v = s

        if max_v < s :
            max_v = s

    print(f'#{tc} {max_v - min_v}')