N, S = map(int, input().split())        # 수열의 개수 N, 부분수열의 원소를 다 더한 값 S 받기
n_li = list(map(int, input().split()))       # 수열을 리스트로 받습니당
n_len = len(n_li)               # 리스트의 길이

# 원하는 합을 만드는 부분수열의 개수를 셀 변수 생성 // 공집합일 경우에는 0으로 취급되어서 S가 0일 경우에는 -1로 해준다.
if S == 0 :
    count = -1

else :
    count = 0

for i in range(1 << n_len) :
    sum_data = 0
    for j in range(n_len) :
        if i & (1<<j) :
            sum_data += n_li[j]

    if sum_data == S :
        count += 1

print(count)