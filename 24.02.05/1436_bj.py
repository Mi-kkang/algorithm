num = 666 * 10000
right_num = []
count = 0

# 0부터 6660000까지 중에서 666이 들어가 있는 숫자를 리스트에 추가한다 // count는 얼마나 나오는지 확인용으로 넣음...
for i in range(num) :
    if '666' in str(i) :
        count += 1
        right_num.append(i)

n = int(input())        # n 입력받기

print(right_num[n-1])