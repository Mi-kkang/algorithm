t = 10      # 테스트 케이스 10번으로 고정

for tc in range(1, t+1) :
    num, password = map(str, input().split())
    real_pw = []        # 원래 패스워드를 담는 리스트를 만든다.

    for idx in password :
        if real_pw :                    # 리스트에 무언가가 하나 이상 들어있을 때,
            if real_pw[-1] == idx :     # 맨 마지막 인자와 비교해서 같을 경우,
                real_pw.pop()

            else :
                real_pw.append(idx)

        else :                          # 리스트에 아무것도 들어있지 않을 경우,
            real_pw.append(idx)

    print(f'#{tc}', end=' ')
    for i in real_pw :
        print(i, end='')

    print()