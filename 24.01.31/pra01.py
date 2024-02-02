'''
3
1 2 3
4 5 6
7 8 9
'''


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [[0] * N for _ in range(N)]
arr3 = [[0]*N] * N      # 얕은 복사가 되기 때문에 결과를 중간에 값을 하나 바꾸면 다 같이 바뀜
print(arr3)         # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
arr3[0][0] = 1      # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
print(arr3)
print(arr2)
arr2[0][0] = 1
print(arr2)