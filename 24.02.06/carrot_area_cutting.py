# 영역을 3개로 나누는 법 // 나누는 기준이 2개이다.
# 당근 문제를 참고하기 위한 어쩌고
N = int(input())
arr = list(map(int, input().split()))

for i in range(N-2) :    # 왼쪽 영역의 마지막 인덱스
    for j in range(i+1, N-1) :
        if arr[i] != arr[i+1] and arr[j] != arr[j+1] :      # 같은 것이 서로 다른 박스에 들어가지 말아야 함
            pass