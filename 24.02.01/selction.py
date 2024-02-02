def selection_sort(a, N) :
    for i in range(N-1) :                       # 구간의 시작 i / 2개의 원소가 남을 때 까지 (1개가 남을 때 까지도 오케이)
        min_dix = i                             # 구간의 최솟값 위치 min_idx, 첫 원소를 최소로 가정
        for j in range(i+1, N) :              # 실제 최솟값을 찾을 위치 j
            if a[min_dix] > a[j] :
                min_dix = j
        a[min_dix], a[i] = a[i], a[min_dix]     # 최솟값을 구간의 맨 앞으로 이동 (자리 맞바꾸기)

    return

N = 5
arr = [1,3,2,5,4]
print(arr)
selection_sort(arr, N)
print(arr)