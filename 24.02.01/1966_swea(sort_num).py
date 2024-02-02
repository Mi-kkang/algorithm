t = int(input())        # 테스트 케이스 숫자 받기

for tc in range(1, t+1) :
    n = int(input())    # 숫자열의 길이 n 받기
    num_list = list(map(int, input().split()))  # 숫자열 리스트로 받기

    for i in range(n-1) :
        min_idx = i         # 최소 숫자가 존재하는 인덱스를 i로 초기화
        for j in range(i+1, n) :
            # i+1 부터 n까지의 인덱스에 해당하는 리스트 인자를 확인한 후 최소 숫자에 저장된 숫자보다 작으면 다시 저장
            if num_list[min_idx] > num_list[j] :
                min_idx = j

        # 반복으로 얻어낸 제일 작은 숫자가 들어간 인덱스를 맨 앞 인덱스에 들어간 값과 교환
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

    print(f'#{tc}', end=' ')

    # 리스트에 들어있는 숫자들을 차례대로 출력
    for n in num_list :
        print(n, end=' ')

    print()