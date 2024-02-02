k = 3
n = 6
arr = [0, 1, 0, 1, 1, 1]
ans = 0
cnt = 0

for i in range(n) :
    if arr[i] == 0 :
        if cnt == k :
            ans += 1
        cnt = 0

    else :  # arr[i] == 1
        cnt += 1
        if i == n-1 :       # if i == n-1 and cnt == k : 로도 쓸 수 있당
            if cnt == k :
                ans += 1

print(ans)