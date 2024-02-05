t = int(input())        # 테스트 케이스 숫자 받기

for tc in range(1, t+1) :
    # 길이가 n인 문자열 str1과 길이가 m인 문자열 str2를 받는다.
    str1 = input()
    str2 = input()

    # str2에 str1과 일치하는 문자열이 있다면 1출력
    if str1 in str2 :
        print(f'#{tc} 1')

    # 아니면 0 출력
    else :
        print(f'#{tc} 0')