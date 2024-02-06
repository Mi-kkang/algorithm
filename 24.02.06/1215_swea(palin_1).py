t = 10          # 테스트 케이스 10개가 주어짐
n = 8           # n x n 배열에서 n이 8로 주어짐

for tc in range(1, t+1) :
    pa_len = int(input())   # 찾아야하는 회문의 길이를 받는다.
    arr = [list(map(str, input())) for _ in range(n)]
    collect = 0             # 회문의 개수를 담는 변수 설정

    for i in range(n) :     # 가로로 회문 찾아보기
        for j in range(n- pa_len + 1) :
            count = 0
            for k in range(pa_len // 2) :
                if arr[i][j+k] == arr[i][j+pa_len-(1+k)] :
                    count += 1

            if count == pa_len // 2 :
                collect += 1

    for j in range(n) :     # 세로로 회문 찾아보기
        for i in range(n- pa_len + 1) :
            count = 0
            for k in range(pa_len // 2):
                if arr[i+k][j] == arr[i + pa_len - (1+k)][j]:
                    count += 1

            if count == pa_len // 2:
                collect += 1


    print(f'#{tc} {collect}')