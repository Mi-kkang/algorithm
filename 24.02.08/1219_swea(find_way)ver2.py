def dfs(s, e) :         # s 출발, e 도착
    visited = [0]*100   # visited, stack 생성 및 초기화
    stack = []
    visited[s] = 1      # 시작점 방문 표시
    v = s               # 현재 방문 위치 v
    while True :        # 탐색
        for w in adjl[v] :
            if visited[w] == 0 :
                stack.append(v)
                v = w
                visited[v] = 1
                break
        else :  # 지나온 곳에서 다시 탐색
            if stack :      # 지나온 곳이 남아있으면
                v = stack.pop()

            else :      # 출발지까지 거슬러와서 가능한 모든 곳을 확인한 경우
                break # while True :
        if v == e :
            return 1
    return 0



t = 10                  # 테스트 케이스 10개 고정

for tc in range(1, t+1) :
    tn, E = map(int, input().split())       # 테스트 케이스 번호, 길이의 총 개수
    arr = list(map(int, input().split()))

    adjl = [[] for _ in range(100)]

    # A = [-1]*100         # A[i] i에 인접한 도시번호
    # B = [-1]*100         # B[i] i에 인접한 도시번호
    for i in range(0, E*2, 2) :
        n1, n2 = arr[i], arr[i+1]       # n1 -> n2 도로가 있음
        adjl[n1].append(n2)

    print(f'#{tn} {dfs(0, 99)}')