def find_max(A): #A는 리스트
    n = len(A) 
    move_count = 0 #이동 연산 횟수
    comp_count = 0 #비교 연산 횟수

    max_value = A[0] # 초기화 (이동 1회)
    move_count += 1

    for i in range(1,n):
        comp_count +=1 #비교 연산 1회 추가
        if A[i] > max_value:
            max_value = A[i] # 이동 연산 1회 추가
            move_count += 1

    return max_value, comp_count, move_count

def selection_sort(arr): # 선택 정렬
    a = arr[:] # 원본 리스트 복사
    n = len (arr) # 배열 크기
    for i in range(n-1): # i번째 위치에서 최소값 삽입
        least_idx = i # 최소값 인덱스
        for j in range(i+1, n): # 미 정렬된 구간 탐색
            if a[j] < a[least_idx]: # 더 작은 최소값 발견
                least_idx = j # 최소값 인덱스 갱신
        
        a[i], a[least_idx] = a[least_idx], a[i] # i번째 위치와 최소값위치 변경
    return a

def insertion_sort(arr): # 삽입정렬
    a = arr[:]
    n = len(arr)
    for i in range(1,n):
        key = a[i] # 삽입할 원소
        j = i-1 # 정렬된 구간의 마지막 인덱스
        while j >= 0 and a[j] > key: # 삽입할 위치 탐색
            a[j+1] = a[j] # 요소를 한칸 뒤로 이동
            j -= 1
        a[j+1] = key
    return a

if __name__ == "__main__":
    data = [3, 9, 2, 7, 5, 10, 4]
#    result, comp, move = find_max(data)
#    print(f"비교 연산 횟수 : {comp}, 이동 연산 횟수 : {move}")
    sorted_data = insertion_sort(data)
    print(sorted_data)
