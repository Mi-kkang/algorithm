t = 1  # 테스트 케이스의 개수 고정
box_num = 100  # 받은 상자 개수 고정

for tc in range(t):
    flat = int(input())  # 평탄화 횟수 입력받기
    box_list = list(map(int, input().split()))  # 박스 높이 리스트 받기
    counts = [0] * box_num

    for i in range(box_num):  # 받은 리스트에서 같은 높이인 것을 카운트에 저장
        counts[(box_list[i] - 1)] += 1

    max_floor = 100  # 최대 층 높이 설정 / 100으로 초기화
    min_floor = 0  # 최소 층 높이 설정 / 0으로 초기화

    max_box = counts[-1]  # 박스 최대 층 개수
    min_box = counts[0]  # 박스 최소 층 개수

    for j in range(1, box_num):
        if min_box >= flat:
            min_floor = j - 1
            break

        min_box += counts[j] + min_box
        counts[j] -= 1

    for k in range(box_num - 2, -1, -1):
        if max_box >= flat:
            max_floor = k + 1
            break

        max_box += counts[k] + max_box
        counts[k] -= 1

answer = max_floor - min_floor

print(answer)
print(max_floor)
print(min_floor)
