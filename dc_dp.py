# =================================================================================================
# 알고리즘 설계 기법 : 분할과 정복
# =================================================================================================
# 1. 배열 합 구하기 문제 : 억지기법

# def sum_vf(arr): # O(len(arr)), 공간복잡도 O(1)
#     total = 0
#     for x in arr:
#         total += x
#     return total

# def sum_dc(arr, left, right): # 시간복잡도 O(n), 시스템 스택 호출 (n)
#     """분할정복 기반 재귀함수"""
#     # 원소가 한개인 경우 - > 이미 정복
#     if left == right:
#         return arr[left] # 종료 조건
#     # 원소가 2개 이상인 셩우 반으로 나누기
#     mid = (left + right) // 2
#     # 왼쪽 부분 문제 배열의 합
#     left_sum = sum_dc(arr, left, mid)
#     # 오른쪽 배열문제의 합
#     right_sum = sum_dc(arr, mid+1, right)
#     # 병합 (두개의 부분문제의 결과를 합침)
#     return left_sum +right_sum

# arr = [5,3,8,4,1,6,2,7]
# print("iterative sum = ", sum_vf(arr))
# print("divide &conquer sum = ",sum_dc(arr,0,len(arr)-1))

# =================================================================================================

# 2. 거듭제곱 계산 문제 : 억지기법 vs 분할(축소) 정복
# def power_bf(x, n): # O(n)
#     # 억지 기법 반복문 구조
#     result = 1.0
#     for _ in range(n):
#         result *= x
#     return result

# def power_dc(x, n): # O(n)
#     # DC의 축소 정복 기반 재귀 구조
#     if n == 1: # 종료조건
#         return x
#     elif n % 2 == 0: # n이 짝수
#         return power_dc(x * x, n//2) # 재귀 호출 절반크기로 감소
#     else:
#         return x * power_dc(x * x, (n - 1) // 2) # 재귀 호출 절반크기로 감소
    
# x = 2.0
# n = 10
# print(f"억지 기법 _x 의 n 거듭 제곱 ({x}, {n} = {power_bf(x, n)})")
# print(f"축소 기법 _x 의 n 거듭 제곱 ({x}, {n} = {power_dc(x, n)})")


# =================================================================================================

# 3. k번째 작은 수를 찾는 문제 (k-th smallest element)
# 1. 분할 함수 정의 - 퀵정렬의 분할 함수 사용
def parition(A, left, right):
    pivot = A[left] # 피벗 설정
    i = left + 1 # 왼쪽 서브리스트 포인터
    j = right # 오른쪽 서브리스트 포인터
    
    while True:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i > j:
            break
        A[i], A[j] = A[j], A[i]
    A[left], A[j] = A[j], A[left]
    return j

# 억지 기법 : 정렬 이용
def kth_smallest_bf(arr,k):
    B = sorted(arr)
    return B[k-1]

# 축소정복 전략 사용 - 재귀함수와 분할함수 이용
def quick_select(A, left, right, k):
    if left == right: # 함수 호출 종료
        return A[left]
    
    #피벗을  배열 A의 첫번쨰 요소로 설정
    pos = parition(A, left, right)
    # pos는 0부터 시작하는 인덱스 -> 순서로 변환시 pos + 1
    # k와 pos + 1을 비교

    if k + left == pos + 1: # case 1 - 피벗이 k번째인 경우
        return A[pos] 
    elif k + left < pos + 1: # case 2 - k번째 작은수가 피펏의 왼쪽에 나타나는 경우
        return quick_select(A, left, pos - 1, k)
    else:
        # case 3 k번째 작은수가 피벗의 오른쪽에 나타나는 경우 k를 갱신
        return quick_select(A, pos + 1, right, k - (pos + 1 - left))

A1 = [7,2,1,8,6,3,5,4,0]
A2 = A1.copy()
k = 3
print("억지기법 : ",  kth_smallest_bf(A1,k))
print("축소정복 : ",  quick_select(A2, 0, len(A2)-1, k))    
print("*"*100)

# =================================================================================================

# 4. merge sort 병합정렬
# 오름차순으로 정렬, 중복된 데이터 허용 안정적 정렬, 추가 메모리 사용
def merge(A,left,mid,right):
    # 1. 임시 리스트 생성 : 크기 = right -left + 1
    sorted_list = [0] *(right - left + 1)
    
    # 2. 두 부분 리스트의 시작 인덱스
    i = left # 왼쪽부분 시작 인덱스
    j = mid + 1 # 오른쪽 부분 시작 인덱스
    k = 0 #임시 리스트의 시작 인덱스
    
    # 3. 두 정렬 리스트를 비교하여 임시 리스트에 기록
    while i <= mid and j <= right :
        if A[i] <= A[j]:
            sorted_list[k] = A[i]
            i += 1
            k += 1
        else:
            sorted_list[k] = A[j]
            j += 1
            k += 1
    
    # 4. 왼쪽 부분 리스트가 남아있는 경우 모두 복사
    while i <= mid:
        sorted_list[k] = A[i]
        i += 1
        k += 1
    
    # 5. 오른쪽 부분 리스트가 남아있는 경우 모두 복사
    while j <= right:
        sorted_list[k] = A[j]
        j += 1
        k += 1
    
    # 6. 임시 리스트의 결과를 원래 리스트 A에 덮어쓰기
    for t in range(k):
        A[left + t] = sorted_list[t]


# 병합 정렬 함수
def merge_sort(A,left, right):
    if left < right: # 항목이 두개 이상인 경우 분할 Ologn
        mid = (left + right) // 2
        # 왼쪽 부분 정렬
        merge_sort(A, left, mid)
        # 오른쪽 부분 정렬
        merge_sort(A, mid + 1, right)
        # 정렬된 두 부분 리스트를 병합 - O(n)
        merge(A,left,mid,right) 

A = [38, 27, 43, 3, 9, 82]
print("정렬 전 : ", A)
merge_sort(A, 0, len(A) - 1)
print("정렬 후 : ", A)
print("*"*100)


# =================================================================================================
# 알고리즘 설계 전략 : 동적 계획법(Dynamic Programing)
# =================================================================================================
# 1. fibonarcci sequence (피보나치 수열) 문제
# (1) 동적계획법 - 메모제이션 방식 - top down 방식

# 전역변수로 메모이제이션 배열 준비 (0~10까지)
mem = [None] * 11

def fib_fp_mem(n):
    if mem[n] is None:
        if n< 2:
            mem[n] = n
        else:
            mem[n] = fib_fp_mem(n-1) + fib_fp_mem(n -2)
    return mem[n]

    
print("n = 6 => fib(6) : ",fib_fp_mem(6))
print("mem = ", mem[:7])
print("*"*100)

# (2) 동적 계획법 - 테이블화 방식 bottom up 방식 - 작은문제부터 큰 문제로 주어진 문제 해결
def fis_dp_tab(n):
    # 1. 1차원 리스트 준비
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 2] + table[i - 1]
    return table

table = fis_dp_tab(6)
print(table[6])
print("table = ", table[:7])
print("*"*100)

# =================================================================================================
# 계단 프로그래밍 과제
# =================================================================================================




def fis_dp_tab(n):
    # 1. 1차원 리스트 준비
    table = [None] * (n + 1)
    table[1] = 1
    table[2] = 2
    for i in range(3, n + 1):
        table[i] = table[i - 2] + table[i - 1]
    return table
    
stairs = input("계단의 개수를 입력하세요 : ")
stairs = int(stairs)
table = fis_dp_tab(stairs)
print(f"{stairs}개의 계단을 오르는방법의 수는 총 {table[stairs]}개 입니다.")
print("*"*100)

#==================================================================
# 2. 0/1 배낭 문제 DP 구현 - 물건의 개수는 n, 배낭의 용량은 W
# DP 테이블 A[i][w] (주어진 남아있는 배낭 용량 w에서 1부터 i 물건을 까지 고려했을 때 얻어지는 배낭의 최대 가치)을 완성.
# 최종 출력값 A[n][W]는 "최대 가치"만 알려줄 뿐, 어떤 물건들을 선택해야 이 값을 만들 수 있는지 알려주지 않음.
"""
동작 방식 요약 : 
1. i: 위에서 아래로, 물건 1개 → n개
2. w: 왼쪽에서 오른쪽으로, 용량 0 → W
3. 각 칸에서 현재 물건의 무게와 남아 있는 배낭의 용량의 크기을 비교해서
- 넣을 수 없으면 위 값 복사
- 넣을 수 있으면
    - 넣는 경우
    - 안 넣는 경우 
    → 더 큰 값으로 갱신
4. 테이블 오른쪽 아래 A[n][W]가 최종 해답
"""
def knapSack_dp(W, wt, val, n):
    # 1. DP 테이블 초기화 : (n+1) X (W + 1)
    A = []
    for i in range(n + 1):          # 행 생성 (0 ~ n)
        row = []
        for w in range(W + 1):      # 열 생성 (0 ~ W)
            row.append(0)           # 모든 값을 0으로 초기화
        A.append(row)

    # 2. DP 테이블 채우기
    for i in range(1, n + 1):       # 물건 index 1~n - 위에서 아래로 진행
        for w in range(1, W + 1):   # 배낭 용량 1~W - 좌에서 우로 진행
            if w < wt[i-1]:         # i번째 물건이 용량 초과해서  넣을 수 없으므로 위 값 복사
                A[i][w] = A[i-1][w]
            else:                   # i번째 물건을 넣을 수 있으면
                valWith = val[i-1] + A[i-1][w - wt[i-1]]  # 넣는 경우
                valWithout = A[i-1][w]                    # 빼는 경우
                A[i][w] = max(valWith, valWithout)        # 더 큰 값을 선택
    
    # 3. 최대 가치와 DP테이블 A 둘 다 반환
    return A[n][W], A


# 테스트 
n = 3
wt = [2, 1, 3]
val = [12, 10, 20]
W = 5

max_value, A = knapSack_dp(W, wt, val, n)

print("1. 최대 가치 =", max_value)
print()
print("2. DP table")
for i in range(4):
    for w in range(6):
        print(A[i][w],  end = "   ")
    print()

print()
print("3. 선택된 물건 역추적 기능")
"""
선택된 물건의 무게만큼 용량을 줄이고, DP 테이블에서 위로 올라가며 계속 확인한다.
"""
selected = []
w = W
# 물건 데이터
items = [("item1", 2, 12), ("item2",1, 10),("item3",3, 20)]

for i in range(n, 0, -1): # DP 테이블을 거꾸로 올라가며 선택된 물건을 하나씩 찾아내는 과정이 필요
    if A[i][w] != A[i-1][w]:         # i번째 물건은 선택되어 가방에 들어감
        name, wt, val = items[i-1]   # i번째 물건을 리스트에 추가
        selected.append(name)  
        w -= wt                      # i번째 물건을 배낭에 넣었으므로 배낭의 용량에서 그 무게만큼 줄어든다.
                                     # 줄어든 나머지 용량 w에서 앞선 물건(i-1번째까지)으로 최대 가치를 만드는 방법 고려
    else:
        pass

selected.reverse()
print("선택된 물건:", selected)




























