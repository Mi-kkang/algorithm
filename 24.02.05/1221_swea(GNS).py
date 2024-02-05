t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    tn, num = map(str, input().split())        # 테스트 케이스 번호와 문자열 개수 받기
    num = int(num)  # 문자열 개수 정수로 바꿔주기
    nu_li = list(map(str, input().split()))    # 문자열 리스트로 받기
    cou_li = [0] * 10                          # 문자열 리스트에 숫자와 매칭되는 문자 개수를 세기 위한 리스트 생성

    # key값이 숫자, value값이 숫자에 맞는 문자로 된 딕셔너리 생성
    num_dict = {}
    num_dict[0] = 'ZRO'
    num_dict[1] = 'ONE'
    num_dict[2] = 'TWO'
    num_dict[3] = 'THR'
    num_dict[4] = 'FOR'
    num_dict[5] = 'FIV'
    num_dict[6] = 'SIX'
    num_dict[7] = 'SVN'
    num_dict[8] = 'EGT'
    num_dict[9] = 'NIN'

    # 문자열 리스트의 인자들을 하나씩 뽑아서 문자에 매칭되는 리스트 인덱스에 맞춰 값을 증가시킨다.
    for st in nu_li :
        if st == 'ZRO' :
            cou_li[0] += 1
        elif st == 'ONE' :
            cou_li[1] += 1
        elif st == 'TWO' :
            cou_li[2] += 1
        elif st == 'THR' :
            cou_li[3] += 1
        elif st == 'FOR':
            cou_li[4] += 1
        elif st == 'FIV':
            cou_li[5] += 1
        elif st == 'SIX':
            cou_li[6] += 1
        elif st == 'SVN':
            cou_li[7] += 1
        elif st == 'EGT':
            cou_li[8] += 1
        elif st == 'NIN':
            cou_li[9] += 1

    print(tn)

    for i in range(10) :
        replay = cou_li[i]
        for j in range(replay) :
            print(num_dict[i], end=' ')     # 문자의 개수가 저장된 숫자만큼 매칭되는 딕셔너리 value값을 출력해준다.