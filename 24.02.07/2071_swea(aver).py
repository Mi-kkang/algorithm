t = int(input())        # 테스크 케이스 받기

for tc in range(1, t+1) :
    n_li = list(map(int, input().split()))      # 숫자 리스트 받기
    n_sum = 0
    count = 0

    for idx in n_li :
        n_sum += idx
        count += 1

    ava = n_sum / count

    ans = round(ava)        # 반올림하는 함수

    # if n_sum % count != 0 :
    #     ans = n_sum // count
    #
    # else :
    #     ans = (n_sum // count) + 1

    print(f'#{tc} {ans}')