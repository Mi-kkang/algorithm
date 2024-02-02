
A = list(map(int,range(1,13)))  # 집합 A를 만들어보자.
a_len = len(A)

T = int(input())    # 테스트 케이스의 개수

for tc in range(1, T+1) :
    N, K = map(int, input().split())    # 부분집합 원소의 수 N, 부분 집합의 합 K
    count = 0

    for i in range(1<<a_len) :
        sum_data = 0
        num = 0
        for j in range(a_len) :
            if i & (1<<j) :
                sum_data += A[j]
                num += 1

        if sum_data == K and num == N :
            count += 1

    print(f"#{tc} {count}")


# 내가 해야 할 것
# 1) 부분집합의 개수로 부분집합의 합을 만들 수 있는 경우의 수를 구한다.
# 2)



# arr = list(range(1,6))
# N_arr = len(arr)
#
#
# for i in range(1<<N_arr):
#     sum_data = 0
#     for j in range(N_arr):
#         if i & (1<<j):
#             sum_data += arr[j]
#             print(arr[j],end=" ")
#     # 비교
