t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    word = input()      # 단어 받기
    n = len(word)
    count = 0           # 회문인지 아닌지 확인하기 위해 변수 생성

    for i in range(n//2) :
        if word[i] == word[n-i-1] :
            count += 1

    if count == n // 2 :
        print(f'#{tc} 1')

    else :
        print(f'#{tc} 0')