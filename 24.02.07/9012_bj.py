op = {')':'('}

t = int(input())
for tc in range(1, t+1) :
    s = input()
    ans = 'YES'
    stack = []
    for x in s :
        if x in '(' : # 여는 괄호면 push()
            stack.append(x)
        elif x in ')' :         # 닫는 괄호면
            if not stack : # (1) 스택이 비어있으면 오류(break) ans = 0
                ans = 'NO'
                break
            else :      # 스택에 여는 괄호가 있으면
                t = stack.pop()
                if t != op[x] : # (2) pop() 해서 짝이 맞지 않으면 오류(break) ans = 0
                    ans = 'NO'
                    break

            # (3) 짝이 맞으면 계속
    else :  # 주어진 입력에 대한 확인이 끝난 경우
        if stack :  # (4) 스택이 비어있지 않으면(여는 괄호) 오류 ans = 0
            ans = 'NO'

    print(f'{ans}')









# bra_dict = {'(' : 1, ')' : -1}      # 딕셔너리 만들어준다.
#
# t = int(input())                    # 테스트 케이스 개수 받기
#
# for tc in range(1, t+1) :
#     bracket = input()               # 괄호문 받아준다.
#     last = 0                        # 마지막이 무엇인지 확인하기 위해 만든 변수
#     cnt = 0                         # 괄호의 개수를 알기 위해 만드는 어쩌고
#     check = 0
#
#     for inza in bracket :
#         if inza == '(' :
#             if last == 0 :
#                 last = bra_dict['(']
#
#             else :


