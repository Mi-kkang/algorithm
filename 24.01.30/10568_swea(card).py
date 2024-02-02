# 최대값이 들어있는 인덱스를 찾을 수 있나?
t = int(input())

for ro in range(t) :
    num = int(input())
    num_word = list(map(int, input()))
    count = [0] * 10
    max_num = 0
    max_num_count = 0

    # list(filter(lambda x : count[x] == max(count), range(len(count))))

    for ind in num_word :
        count[ind] += 1

    # print(count)

    max_list = list(filter(lambda  x : count[x] == max(count), range(len(count))))

    # print(max_list)

    for idn in count :
        if idn >= max_num_count :
            max_num_count = idn
            max_num = max(max_list)





    print(f'#{ro+1} {max_num} {max_num_count}')



# 가장 큰 수는 어디에 들어있을까...
N = 5
arr = [ 1, 3, 2, 5, 4 ] # 같은 숫자가 없는 경우

max_idx = 0     # 첫 번째 원소를 가장 큰 수의 위치로 가정
for i in range(1, N) :
    if arr[max_idx] < arr[i] :      # arr[i]가 더 크면
        max_idx = i                 # 최댓값의 위치를 i로 변경

    # if arr[max_idx] <= arr[i] :      # <= 최댓값이 여러개인 경우 가장 오른쪽쪽
    #     max_idx  i                 # 최댓값의 위치를 i로 변경
