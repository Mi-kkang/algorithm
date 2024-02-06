t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    a, b = input().split()      # 전체 문자열 a와 나눌 문자열 b을 받는다.
    n_a = len(a)
    n_b = len(b)
    count = 0           # b를 사용하는 횟수를 담을 변수를 만든다.

    for i in range(n_a - n_b + 1) :
        word = ''
        for j in range(n_b) :
            word += a[i+j]      # a의 인자 하나씩 뺀 후 b의 길이만큼 붙여서 새로운 단어를 만든다.

        # print(word)

        # 새로 만든 단어를 b와 비교해서 같다면 횟수를 하나 올려준다.
        if word == b :
            count += 1

    # a의 길이에서 b를 사용한 횟수(b의 길이를 곱해야 한다)를 빼주면 남은 타이핑 수가 나온다.
    rest = n_a - (count * n_b)

    print(f'#{tc} {count + rest}')