# 5 x 5 2차 배열에 25개의 숫자를 저장하고,
# 대각선 원소의 합을 구하시오. 대각선 원소는 다음과 같은 위치의 원소를 나타낸다.

# 내가 풀어야 할 것
# 1. 2차원 배열에 25개의 숫자를 저장한다
# 2. 대각선 원소의 리스트를 만든다? 정방향 대각선과 반대쪽 대각선을 따로 구해야 할 듯?
# 3. 구한 대각선 원소의 리스트를 다 더한 후 겹쳐지는 부분 (2, 2) 에 들어있는 수를 빼준다.

# N = 5
# arr = [[0] * N for _ in range(N)]
# num = 0
#
# for i in range(N) :
#     for j in range(N) :
#         num += 1
#         arr[i][j] = num
N = int(input())
# 테스트 케이스 입력받은거 2차원 배열에 저장
arr = [list(map(int, input().split())) for _ in range(N)]

# print(arr)
for_cross = []  # 정방향 크로스 값 넣을 리스트 생성
bac_cross = []  # 역방향 크로스 값 넣을 리스트 생성

# 정방향, 역방향 크로스 값 각각의 리스트에 넣기
for i in range(N) :
    for j in range(N) :
        if i == j :
            for_cross.append(arr[i][j])

        if i + j == (N-1) :
            bac_cross.append(arr[i][j])

# print(for_cross)
# print(bac_cross)

count = 0       # 안에 들어있는 인자가 몇 개인지 확인하기 위한 변수 생성 (가운데 겹치는 값 인덱스 알아보기 위한 수)
mlt_ans = 0     # 대각선에 있던 값들 모두 더할 값 저장

# 정방향 크로스 리스트에 있는 값들 하나씩 더해주기 + 리스트 안 인자 개수 확인하기
for n in for_cross :
    count += 1
    mlt_ans += n

# 역방향 크로스 리스트에 있는 값들 하나씩 더해주기 // 리스트 안 인자의 개수는 이미 구해서 괜찮다.
for nu in bac_cross :
    mlt_ans += nu

count //= 2

mlt_ans = mlt_ans - for_cross[count]

# print(for_cross[count])
print(mlt_ans)


# 강사님 솔루션
# 연습문제 1-1
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# total = 0
#
# for i in range(N):
#     total += arr[i][i]  # 오른쪽 아래 대각선
#     total += arr[i][N - 1 - i]
#
# if N % 2:   # 크기가 홀수인 경우
#     total -= arr[N // 2][N // 2]    # 중심 원소가 중복되므로
#
# print(total)