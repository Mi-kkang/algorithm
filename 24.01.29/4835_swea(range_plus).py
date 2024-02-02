t = int(input())

for replay in range(t) :

    n, m = map(int, input().split())

    count_list = list(map(int, input().split()))

    mul_list = []

    for num in range(n-(m-1)) :

        mul_num = 0

        for count in range(m) :
            mul_num += count_list[num+count]

        # print(mul_num)
        mul_list.append(mul_num)

    mul_max = mul_list[0]
    mul_min = mul_list[0]

    for idn in mul_list :
        if idn > mul_max :
            mul_max = idn

        if idn < mul_min :
            mul_min = idn

    answer = mul_max - mul_min

    print(f'#{replay+1} {answer}')