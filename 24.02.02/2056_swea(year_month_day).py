t = int(input())        # 테스트 케이스 개수 입력받기

for tc in range(1, t+1) :
    cal_li = list(input())      # 달력 숫자를 리스트로 받는다.

    # 형식이 정해져 있기 때문에(8자리) 자리에 맞춰 더해서 년, 월, 일을 만든다.
    year = cal_li[0]+cal_li[1]+cal_li[2]+cal_li[3]
    month = cal_li[4]+cal_li[5]
    day = cal_li[6]+cal_li[7]

    # 조건을 확인해서 그 조건에 맞으면 날짜를 출력, 아니라면 -1을 출력한다.
    if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12 :
        if 1<= int(day) and int(day) <=31 :
            print(f'#{tc} {year}/{month}/{day}')

        else :
            print(f'#{tc} -1')

    elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11 :
        if 1<= int(day) and int(day) <=30 :
            print(f'#{tc} {year}/{month}/{day}')

        else :
            print(f'#{tc} -1')

    elif int(month) == 2 :
        if 1<= int(day) and int(day) <=28 :
            print(f'#{tc} {year}/{month}/{day}')

        else :
            print(f'#{tc} -1')

    else :
        print(f'#{tc} -1')