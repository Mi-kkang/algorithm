t = int(input())        # 테스트 케이스의 개수

for tc in range(1, t+1) :
    n = int(input())        # 노선의 개수
    stop_bus = []           # 멈추는 정류장을 저장하는 리스트

    for i in range(n) :
        A, B = map(int, input().split())    # 시작 정류장, 끝 정류장 입력 받기

        for i in range(A, B+1) :
            stop_bus.append(i)


    p = int(input())        # 버스 정류장의 개수를 받아온다.

    bus_go = []             # 정류장을 지나는 버스의 개수를 저장하는 리스트 생성

    for j in range(1, p+1) :
        c = int(input())
        bus_go.append(0)


    for i in range(len(stop_bus)) :
        for