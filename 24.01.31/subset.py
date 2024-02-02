N = 3
arr = [1, 2, 3]

for i in range(1<<N) : # 2의 n 제곱에서 이동하는 것이다...?
    s = 0
    for j in range(N) :     # i 가 사용할
        if i & (1<<j) :     # 0 또는 0이 아닌 값이 나온다.
            s += arr[j]
            print(arr[j], end=' ')

    print(s)