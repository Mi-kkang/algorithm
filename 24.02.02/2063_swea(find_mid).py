n = int(input())        # 받아올 숫자의 개수를 나타내는 수를 받아온다.
sc_li = list(map(int, input().split()))     # 나열된 숫자들을 리스트로 받는다.
find = n // 2
print(find)
print(sc_li[find+1])