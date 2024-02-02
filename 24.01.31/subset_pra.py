'''
10
-7 -5 2 3 8 -2 4 6 9
'''

def f(arr, N) :
    for i in range(1, 1 << N):  # 2의 n 제곱에서 이동하는 것이다...?
        s = 0
        for j in range(N):  # i 가 사용할
            if i & (1 << j):  # 0 또는 0이 아닌 값이 나온다.
                s += arr[j]

        if s == 0 :
            return  True

    return  False


N = int(input())
arr = list(map(int, input().split()))
print(f(arr, N))

