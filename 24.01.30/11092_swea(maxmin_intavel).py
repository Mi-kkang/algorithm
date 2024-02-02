t = int(input())    # 테스트케이스 개수 받기

for n in range(t) :
    num = int(input())
    num_list = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0

    for i in range(num) :
        if num_list[max_idx] <= num_list[i] :
            max_idx = i

        if num_list[min_idx] > num_list[i] :
            min_idx = i

    if max_idx > min_idx :
        answer = max_idx - min_idx

    elif min_idx >= max_idx :
        answer = min_idx - max_idx

    print(f'#{n+1} {answer}')



# # 가장 큰 수는 어디에 들어있을까...
# N = 5
# arr = [ 1, 3, 2, 5, 4 ] # 같은 숫자가 없는 경우
#
# max_idx = 0     # 첫 번째 원소를 가장 큰 수의 위치로 가정
# for i in range(1, N) :
#     if arr[max_idx] < arr[i] :      # arr[i]가 더 크면
#         max_idx = i                 # 최댓값의 위치를 i로 변경
#
#     # if arr[max_idx] <= arr[i] :      # <= 최댓값이 여러개인 경우 가장 오른쪽쪽
#     #     max_idx  i                 # 최댓값의 위치를 i로 변경

# t = int(input())
# for tc in range(1, t+1) :
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     min_idx = 0     # 맨 앞을 최솟값 위치로 가정
#     max_idx = 0     # 맨 앞을 최댓값 위치로 가정
#
#     for i in range(n) :
#         # 가장 작은 수가 여러 개이면 먼저 나오는 위치 >
#         if arr[min_idx] > arr[i] :      # 지금까지의 최솟값보다 arr[i]가 더 작으면
#             min_idx = i
#
#         # 가장 큰 수가 여러 개이면 마지막으로 나오는 위치 <=
#         if arr[max_idx] <= arr[i] :
#             max_idx = i
#
#
#     ans = max_idx - min_idx if max_idx > min_idx else min_idx - max_idx
#     print(f'#{tc} {ans}')