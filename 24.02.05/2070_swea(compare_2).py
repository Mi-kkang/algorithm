t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    a, b = map(int,input().split())     # 숫자 2개 받기

    if a > b :
        print(f'#{tc} >')

    elif a < b :
        print(f'#{tc} <')

    else :
        print(f'#{tc} =')