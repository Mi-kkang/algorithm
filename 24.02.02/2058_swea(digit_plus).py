n_li = list(map(int, input()))        # 숫자를 리스트로 입력받는다.
n_sum = 0                             # 각 자리의 합을 저장할 변수를 생성한다.

# 받은 리스트를 반복문으로 돌면서 각 인자를 합을 저장할 변수에 더해준다.
for i in n_li :
    n_sum += i

print(n_sum)