w_chess = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

b_chess = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

n, m = map(int, input().split())
original = [list(map(str, input())) for _ in range(m)]
new_arr = [['0']* 8 for _ in range(8)]
min_count = 64      # 다 바꾸는 경우가 8 x 8 = 64 이기 때문에 64로 정했다.
print(new_arr)

for i in range(m-8) :
    for j in range(n-8) :

        for k in range(8) :
            for l in range(8) :
                new_arr[k][l] = original[i+k][j+l]


        print(new_arr)


#         for k in range(8) :
#             for l in range(8) :
#                 new_arr[k][l] = original[i+k][j+l]
#
#         if new_arr[0][0] == 'W' :
#             for p in range(8) :
#                 count = 0
#                 for q in range(8) :
#                     if new_arr[p][q] != w_chess[p][q] :
#                         new_arr[p][q] = w_chess[p][q]
#                         count += 1
#                 if min_count > count :
#                     min_count = count
#
#         elif new_arr[0][0] == 'B' :
#             for p in range(8) :
#                 count = 0
#                 for q in range(8) :
#                     if new_arr[p][q] != b_chess[p][q] :
#                         new_arr[p][q] = b_chess[p][q]
#                         count += 1
#                 if min_count > count :
#                     min_count = count
#
# print(min_count)
