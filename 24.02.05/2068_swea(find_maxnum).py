t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    num_li = list(map(int, input().split()))   # 숫자들을 리스트로 받아서 저장한다.

    num_ma = 0          # 제일 큰 수를 찾기 위한 변수 생성 / 0으로 초기화

    for nu in num_li :
        if num_ma < nu :
            num_ma = nu

    print(f'#{tc} {num_ma}')