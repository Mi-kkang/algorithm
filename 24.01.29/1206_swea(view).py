import sys
sys.stdin = open('input_view.txt', 'r')

t = 10

for test in range(1, t+1) :
    n = int(input()) # 건물 개수
    building = list(map(int, input().split()))

    view_good = 0 # 조망권의 합

    for ch in range(2, n-2) :  # for i : 2 -> N-3
        max_height = building[0]
        behind_height = 0
        forward_height = 0
        if building[ch-2] >= building[ch-1] :
            behind_height = building[ch-2]

        else :
            behind_height = building[ch-1]


        # if / else 문을 줄이는 법!
        # behind_height = building[ch-1]
        #
        # if building[ch-2] >= building[ch-1] :
        #     behind_height = building[ch-2]

        if building[ch + 2] >= building[ch + 1]:
            forward_height = building[ch + 2]

        else:
            forward_height = building[ch + 1]

        if behind_height >= forward_height :
            max_height = behind_height

        else :
            max_height = forward_height

        # max_height 를 구하는 법 / 코드 줄이기
        # max_height = behind_height if behind_height > forward_height else forward_height

        if building[ch] > max_height :
            view_good += (building[ch] - max_height)

    print(f'#{test} {view_good}')