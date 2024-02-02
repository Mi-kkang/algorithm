# t = int(input())    # 주어진 노선 수
#
# for ro in range(t) :
#     k, n, m = map(int, input().split())
#     # k = 한번 충전해서 이동할 수 있는 최대 정류장 수, n = 종점 정류장(정류장 수), m = 충전기가 설치된 정류장 개수
#     m_list = list(map(int, input().split()))    # 충전기가 설치된 정류장 위치 리스트
#
#     dis_list = []   # 충전기 있는 정류장 사이의 거리의 차를 넣은 리스트
#
#     dis_list.append(m_list[0])      # 출발지에서 첫번째 충전기 사이의 거리를 추가시켜 준다.
#
#     for i in range(m-1) :   # 충전기 있는 정류상 사이의 거리 차를 구해서 리스트로 넣는다.
#         dis = m_list[i+1] - m_list[i]
#         dis_list.append(dis)
#
#     dis_list.append(n-(m_list[-1]))     # 마지막 충전기가 설치된 정류장에서 종점까지의 거리도 추가시켜 준다.
#
#     count = 0       # 충전 횟수를 넣을 변수를 생성 / 0으로 초기화
#     gas = k
#
#     for n in range(m) :      # 충전기가 설치된 정류장 개수 거리 +2 만큼 반복문 돌리기
#         # m+1 인 이유 << 출발지에서 첫번째 충전기 거리와 마지막 충전기에서 종점까지의 거리도 추가했기 때문에
#         if gas - dis_list[n] > dis_list[n+1] :
#             gas -= dis_list[n]
#             continue
#
#         elif gas - dis_list[n] < dis_list[n+1] :
#             gas = gas - dis_list[n] + k
#             count += 1
#
#
#
#
#     print(count)
    # print(dis_list)

    # 내가 해야 할 것
    # 1. 충전기가 설치된 정류장 위치 리스트를 통해 다음 충전기까지의 거리를 구한다
    # 만약, 그 거리가 최대 이동 수 보다 작을 때, 이전 정류장에서 보충해서 와야한다. (거리가 얼마나 짧던지간에)
    # 그렇게 얼마나 많은 정류장을 가야하는지 확인해보고, 그 뒤 그 개수를 저장해 출력한다.


# ver 1

# t = int(input())
# for tc in range(1, t+1) :
#     k, n, m = map(int, input().split())     # k 최대 이동거리, n 종점번호, m 충전기 개수
#     charger = list(map(int, input().split()))
#
#     busstop = [0] * (n+1)       # 충전기가 있는지 정류장별로 표시
#     for x in charger :
#         busstop[x] = 1
#
#     bus = 0     # 버스의 현재 위치
#     count = 0   # 충전횟수
#     while bus + k < n :     # 마지막 충전이후 종점에 도착할 수 없으면 계속 도는 것이다.
#         # 가장 먼 충전기를 찾으면 count +=1 / bus 이동
#         last = 0
#         for i in range(bus+1, bus+k+1) :  # bus -> bus + k 사이 마지막 충전기 i 위치 찾기
#             if busstop[i] :        # i 정류장에 충전기가 있으면
#                 last = i
#
#         # 충전기가 없으면
#         if last == 0 :
#             count = 0
#             break
#
#         else :  # 충전기가 있으면 (운행할 수 있는 최대 거리이내의 마지막 충전기)
#             bus = last
#             count += 1
#
#     print(f'#{tc} {count}')


# ver 2
t = int(input())
for tc in range(1, t+1) :
    k, n, m = map(int, input().split())  # k 최대 이동거리, n 종점번호, m 충전기 개수
    charger = [0] + list(map(int, input().split())) + [n]

    last = 0        # 마지막 충전 위치, 초기값은 출발점 0 // charger[0] 도 똑같음
    count = 0       # 충전횟수
    for i in range(1, m+2) :    # 모든 충전기 위치 charger[i]에 대해 확인해볼 예정
        if (charger[i] - charger[i-1]) <= k :   # 충전기 사이는 운행 가능
            if (charger[i] - last) > k :    #충전기 사이 운행은 가능하나, 마지막 충전기에서 너무 멀면 충전을 해야 함
                last = charger[i-1]
                count += 1

        else :
            count = 0
            break


    print(f'#{tc} {count}')