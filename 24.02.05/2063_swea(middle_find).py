n = int(input())        # 입력받는 숫자의 수 / 항상 홀수로 주어진다.
n_li = list(map(int, input().split()))      # 나열된 숫자들을 리스트로 받는다.

for i in range(n-1, -1, -1) :
    for j in range(n-1) :
        if n_li[j] > n_li[j+1] :
            n_li[j], n_li[j+1] = n_li[j+1], n_li[j]


print(n_li[n//2])