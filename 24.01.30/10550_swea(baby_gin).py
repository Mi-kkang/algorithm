t = int(input())    # 입력된 테스트케이스 수 받기

for ro in range(t) :   # 입력된 테스트 케이스 수 만큼 반복문 돌리기
    card = int(input())     # 숫자 받기
    count = [0] * 12    # 각 자리 수를 누적하기 위해 만들어둔 숫자 리스트

    for n in range(6) :     # 각 자리의 수를 반복문을 통해 맞는 자리에 저장
        count[card % 10] += 1
        card //= 10

    num = 0
    tri = 0  # triplet 개수 / 0으로 초기화
    ru = 0  # run 개수 / 0으로 초기화

    while num < 10 :
        if count[num] >= 3 :
            count[num] -= 3
            tri += 1
            continue

        if count[num] >= 1 and count[num+1] >= 1 and count[num+2] >= 1 :
            count[num] -= 1
            count[num+1] -= 1
            count[num+2] -= 1
            ru += 1
            continue
        num += 1

    if ru + tri == 2 :
        print(f'#{ro+1} Baby Gin')

    else :
        print(f'#{ro+1} Lose')