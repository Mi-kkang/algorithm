def dfs(i, V, last) :     # 우리가 원하는 시작 i(S), 마지막 V(V), 우리가 원하는 마지막 곳 last(G)
    visited = [0] * (V+1)   # visited, stack 생성 및 초기화
    st = []
    visited[i] = 1          # 시작점 방문
    # print(i)                # 정점에서 할 일 (출력)
    while True :            # 탐색
        for w in adjl[i] :  # 현재 방문한 정점에 인접하고 방문 안 한 정점 w가 있으면
            if visited[w] == 0 :
                st.append(i)    # push(i), i를 지나서
                i = w           # w에 방문
                visited[i] = 1  # 방문에서 할일 // i에 w를 할당했기 때문에 i든 w를 쓰든 상관 없다!
                break           # for w
        else :              # for w에 대한 else, i에 남은 인접 정점이 없으면
            if st :         # 스택이 비어있지 않으면(지나온 정점이 남아있으면)
                i = st.pop()
            else :          # 스택이 비어있으면(출발점에서 남은 정점이 없으면)
                break      # while True
        if i == last:  # 만약 방문한 곳이 마지막 점과 같다면 그 지점을 리턴해준다.
            result = 1
            break
        else :
            result = 0

    return result



t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    V, E = map(int, input().split())        # V개 이내의 노드 / E개의 간선 받기
    adjl = [[] for _ in range(V+1)]

    for i in range(E) :
        n1, n2 = map(int, input().split())  #  출발 노드, 도착 노드 나눠서 받기!
        adjl[n1].append(n2)

    # print(adjl)

    S, G = map(int, input().split())        # 출발 노드 S와 도착 노드 G를 받는다.

    ans = dfs(S, V, G)

    print(f'#{tc} {ans}')