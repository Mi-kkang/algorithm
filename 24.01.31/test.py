arr = list(range(1,6))
N_arr = len(arr)


for i in range(1<<N_arr):
    sum_data = 0
    for j in range(N_arr):
        if i & (1<<j):
            sum_data += arr[j]
            print(arr[j],end=" ")

    print()
    # 비교



