# 숫자 배열 회전

def rotate(dest, src) :
    for i in range(n) :
        for j in range(n) :
            dest[j][n-1-i] = src[i][j]


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr90 = [[0]*n for _ in range(n)]
    rotate(arr90, arr)

    print(f'#{tc}')
    for i in range(n) :
        for j in range(n) :
            print(arr[i][j], end='')
        print(end=' ')

        for j in range(n) :
            print(arr90[i][j], end='')
        print(end=' ')

        for j in range(n) :
            print(arr[i][j], end='')
        print(end=' ')

        print()

# 서로 다른 떨어져 있는 것들을 붙여서 프린트 할 수 있는 방법
# a = ['1', '2', '3']
# s = ''.join(a)
# print(s)
#
# b = [1, 2, 3]
# s2 = ''.join(map(str, b))
# print(s2)