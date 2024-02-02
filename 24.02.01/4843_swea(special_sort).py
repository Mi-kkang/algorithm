t = int(input())        # 테스트 케이스 숫자 받기

for tc in range(1, t+1) :
    n = int(input())        # 정수의 개수 받기
    num_li = list(map(int, input().split()))    # 숫자열 리스트 받기

    for i in range(n) :
        # 인덱스 값이 0이거나 짝수일 때, 최대 값을 넣기
        if i == 0 or i % 2 == 0 :
            max_idx = i
            for j in range(i+1, n) :
                if num_li[max_idx] < num_li[j] :
                    max_idx = j

            num_li[i], num_li[max_idx] = num_li[max_idx], num_li[i]

        # 인덱스 값이 홀수일 때, 최소 값을 넣기 // else로도 가능
        elif i % 2 == 1 :
            min_idx = i
            for j in range(i + 1, n):
                if num_li[min_idx] > num_li[j]:
                    min_idx = j

            num_li[i], num_li[min_idx] = num_li[min_idx], num_li[i]

    print(f'#{tc}', end=' ')
    for li in range(10) :
        print(num_li[li], end=' ')

    print()