t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    n = int(input())    # 수열의 길이 받기
    n_li = list(map(int, input()))    # 길이 n인 수열 받기

    max_v = 0   # 연속한 1의 개수 중 최대값을 넣기 위한 변수 생성 / 0으로 초기화
    cnt = 0     # 연속한 1의 개수를 세기 위한 변수 생성 / 0으로 초기화

    for i in range(n) :
        if n_li[i] == 0 :       # 리스트에 저장된 인덱스에 대응되는 숫자가 0일 경우
            if max_v < cnt :    # 바로 전 까지의 cnt 와 최대값이 저장된 값을 비교해서 cnt 가 더 클 경우,
                max_v = cnt     # 최대값을 cnt 로 재할당 한다.
            cnt = 0             # 0을 만났기 때문에 연속한 1의 개수는 초기화 해준다.

        else :  # n_li[i] == 1 일 경우
            cnt += 1
            if i == n-1 :   # 수열의 마지막 값이 1일 경우, 0을 만나지 않기 때문에 max_v와 비교가 안된다. 그걸 비교해주기 위한 조건문
                if max_v < cnt :
                    max_v = cnt

    print(f'#{tc} {max_v}')