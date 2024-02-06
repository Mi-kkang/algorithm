t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    a, b = input().split()      # 전체 문자열 a와 나눌 문자열 b을 받는다.
    n_a = len(a)
    n_b = len(b)
    count = 0           # b를 사용하는 횟수를 담을 변수를 만든다.
    i = 0

    while i  <= (n_a - n_b) :
        word = ''
        for j in range(n_b) :
            word += a[i+j]      # a의 인자 하나씩 뺀 후 b의 길이만큼 붙여서 새로운 단어를 만든다.

        # print(word)

        # 새로 만든 단어를 b와 비교해서 같다면 횟수를 하나 올려준다.
        if word == b :
            count += 1
            i += n_b

        else :
            i += 1

    # n = a.count(b) ==> 내장 함수를 쓸 경우 이것과 같은 값이다. # 찾은 문자열 다음부터 검색
    # a = a.replace(b, 'b') ==> 이렇게 쓸 경우에도 가능하다! 이건 길이가 그냥 len(a) 가 될 것!

    # a의 길이에서 b를 사용한 횟수(b의 길이를 곱해야 한다)를 빼주면 남은 타이핑 수가 나온다.
    rest = n_a - (count * n_b)

    print(f'#{tc} {count + rest}')

    # print(f'#{tc}', len(a.replace(b, 'b'))) << 이걸로 하면 한번에 나오기 가능... 기능성 끝판왕ㅋㅋㅋ



# 강사님 솔루션
# t = int(input())
# for tc in range(1, t+1) :
#     A, B = input().split()
#     N = len(A)
#     M = len(B)
#     cnt = 0
#     i = 0       # A에서 비교시작위치
#     j = 0       # B에서의 비교위치
#     while i <= N-M :            # B의 길이만큼인 마지막 구간의 시작 위치
#         if A[i][j] == B[j] :    # 같은 글자면
#             j += 1
#             if j == M :         # B의 마지막 글자인 경우
#                 cnt += 1        # 단축키 횟수
#                 j = 0           # 패턴을 찾은 경우
#                 i += M
#         else :
#             j = 0
#             i += 1
#
#     print(f'#{tc} {N - (M*cnt) + cnt}')