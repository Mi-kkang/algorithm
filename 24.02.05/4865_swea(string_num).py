t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    # 길이가 n인 문자열 str1과 길이가 m인 str2를 받는다.
    str1 = list(set(input()))   # 안에 들어있는 중복 문자를 제거한 후 리스트화 해준다.
    str2 = input()

    # 가장 많은 글자의 수를 저장하기 위해 변수 생성 / 0으로 초기화
    max_str = 0

    for st in str1 :
        num = 0
        for idx in str2 :
            if idx == st :  # str2에 있는 문자가 str1의 문자와 같을 경우
                num += 1

        if max_str < num :
            max_str = num

    print(f'#{tc} {max_str}')