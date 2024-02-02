# 내가 해야 하는 것
# 5 x 5 2차 배열에 25개의 숫자를 저장하고,
# 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.

# 1) 인접한 요소들을 구하기 위해서, 인접한 요소로 이동했을 때의 행과 열의 좌표 차이를 미리 저장한다.
# 2) 배열 차수 N을 구하고(여기서는 5로 지정되어 있음) 각 배열 안에 들어갈 숫자를 받고 저장한다.
# 3) 완성된 배열을 반복문을 돌려 인접한 요소를 찾고, 그 뒤 원래 시작점의 값을 뺀 절대값을 구한 후 다 더해준다.
# +) 여기서 중요한 점은 인접한 요소가 배열 범위 밖일 경우는 취급하지 않는다는 점이다!!!

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# print(arr)

result = 0

for i in range(N) :
    for j in range(N) :
        # abs_li = []
        for k in range(4) :
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N :
                result += abs(arr[i][j] - arr[ni][nj])
                # abs_li.append(ans)
                # result += ans

print(result)





# 강사님 솔루션 ver 1
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]   # 5x5 2차 배열에 25개의 숫자를 저장하고
# total = 0
# for i in range(N) :     # 25개의 각 요소에 대해서
#     for j in range(N) :
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]] :   # 그 요소와 이웃한(상하좌우) 요소 arr[ni][nj]를 구해야 한다.
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N :
#                 total += abs(arr[ni][nj] - arr[i][j])     # 차의 절대값을 구하시오, 총합을 구하시오.
#
# print(total)



# 강사님 솔루션 ver2
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]   # 5x5 2차 배열에 25개의 숫자를 저장하고
# total = 0
# for i in range(N) :     # 25개의 각 요소에 대해서
#     for j in range(N) :
#         for k in range(4) :
#             ni = i + di[k]
#             nj = j + di[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 total += abs(arr[ni][nj] - arr[i][j])
#
# print(total)