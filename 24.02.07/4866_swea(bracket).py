bra_dict = {'{' : 1, '}' : -1, '(' : 2, ')' : -2}   # 딕셔너리를 만들어준다


t = int(input())            # 테스트 케이스 횟수 받기

for tc in range(1, t+1) :
    word = input()          # 괄호 어쩌고 받기
    last = 0                # 마지막에 어떤 괄호가 나왔는지 확인하기 위해 만든 변수
    mul = 0                 # 괄호에 대한 점수들을 다 합하기 위해 만든 변수
    check = 0

    for inza in word :
        if inza == '{' :
            last = bra_dict['{']
            mul += last


        elif inza =='}' :
            if last == 0 :
                check = -1
                break
            elif last == 2 :
                check = -1
                break
            else :
                last = bra_dict['}']
                mul += last

        elif inza == '(' :
            last = bra_dict['(']
            mul += last


        elif inza == ')' :
            if last == 0 :
                check = -1
                break
            elif last == 1 :
                check = -1
                break
            else :
                last = bra_dict[')']
                mul += last

        else :
            continue

    if check == -1 :
        print(f'#{tc} 0')

    else :
        if mul == 0 :
            print(f'#{tc} 1')

        else :
            print(f'#{tc} 0')


# op = {')':'(', '}':'{'}
#
# t = int(input())
# for tc in range(1, t+1) :
#     s = input()
#     ans = 1
#     stack = []
#     for x in s :
#         # if x in '{}()' :   # 괄호인 경우
#         if x in '{(' : # 여는 괄호면 push()
#             stack.append((x))
#         elif x in '})' :         # 닫는 괄호면
#             if not stack : # (1) 스택이 비어있으면 오류(break) ans = 0
#                 ans = 0
#                 break
#             else :      # 스택에 여는 괄호가 있으면
#                 t = stack.pop()
#                 if t != op[x] : # (2) pop() 해서 짝이 맞지 않으면 오류(break) ans = 0
#                     ans = 0
#                     break
#
#             # (3) 짝이 맞으면 계속
#     else :  # 주어진 입력에 대한 확인이 끝난 경우
#         if stack :  # (4) 스택이 비어있지 않으면(여는 괄호) 오류 ans = 0
#             ans = 0
#
#     print(f'#{tc} {ans}')