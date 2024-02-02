t = int(input())  # 테스트 케이스 개수 받기

for tc in range(1, t + 1):
    n = int(input())  # n x n 배열을 만들 정수 n을 입력 받기
    num_li = list(map(int, range(1, (n * n) + 1)))  # 배열 안에 넣을 숫자 리스트로 생성하기 1~ n*n 까지
    arr = [[0] * n for _ in range(n)]  # 안에 든 숫자가 모두 0인 n x n 배열을 만든다.

    # 진행 방향을 정하기 위한 행과 열을 리스트로 만들어준다.
    # 이동방향이 오른쪽, 아래, 왼쪽, 위 순으로 규칙적이다!
    move_ro = [0, -1, 0, 1]
    move_co = [1, 0, -1, 0]

    ro_m, co_m = 0, 0   # 행과 열 처음 시작점을 설정해준다.
    start = 0  # 숫자 리스트의 인덱스를 처음에 0으로 설정

    arr[ro_m][co_m] = num_li[start]     # 처음 위치 (0, 0)의 자리에 들어갈 숫자 설정
    start += 1

    # 처음 가는 이동방향 설정
    ro = 0
    co = 0

    # 숫자를 넣어둔 리스트의 인덱스 값이 배열 개수가 되기 전까지 반복한다.
    while start < n*n :
        # print(start)
        # 현재 행과 열에서 이동을 시켜준다.
        ro_m += move_ro[ro]
        co_m += move_co[co]

        # print(ro_m, co_m)

        # 만약 행과 열이 배열 안에 존재하고 있을 경우,
        # 배열에 다른 값이 저장되지 않았을 때 (처음값 0이 있을 때)
        # 인덱스에 할당된 숫자 리스트의 값을 저장해주고 인덱스의 값을 하나 증가시킨다.
        if 0 <= ro_m < n and 0 <= co_m < n :
            if arr[ro_m][co_m] == 0 :
                arr[ro_m][co_m] = num_li[start]
                # print(num_li[start])
                start += 1

            # 만약 이미 다른 값이 저장되어 있을 경우, 움직임을 뒤로 무르고 방향을 설정해준다.
            else :
                ro_m -= move_ro[ro]
                co_m -= move_co[co]

                if ro == 3 and co == 3 :
                    ro = 0
                    co = 0

                else :
                    ro += 1
                    co += 1

                # ro = (ro+1) % 4
                # co = (co+1) % 4
                # 이런 식으로도 가능

        # 배열의 범위에서 벗어난 경우, 움직임을 무르고 이동방향을 조정해준다.
        elif 0 <= co_m < n and ro_m >= n :
            ro_m -= move_ro[ro]
            co_m -= move_co[co]
            ro = 1
            co = 1


        elif 0 <= ro_m < n and co_m >= n :
            ro_m -= move_ro[ro]
            co_m -= move_co[co]
            ro = 2
            co = 2

        elif 0 <= co_m < n and ro_m < 0 :
            ro_m -= move_ro[ro]
            co_m -= move_co[co]
            ro = 3
            co = 3

        elif 0 <= ro_m < n and co_m < 0 :
            ro_m -= move_ro[ro]
            co_m -= move_co[co]
            ro = 0
            co = 0


    print(f'#{tc}')

    for i in range(n) :
        for j in range(n) :
            print(arr[i][j], end=' ')

        print()