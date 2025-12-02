# =================================================================================================
# 알고리즘 설계 기법 : 분할과 정복
# =================================================================================================
# 1. 배열 합 구하기 문제 : 억지기법

# def sum_vf(arr): # O(len(arr)), 곡간복잡도 O(1)
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


# 2. 거듭제곱 계산 문제 : 억지기법 vs 분할(축소) 정복
def power_bf(x, n): # O(n)
    # 억지 기법 반복문 구조
    result = 1.0
    for _ in range(n):
        result *= x
    return result

def power_dc(x, n): # O(n)
    # DC의 축소 정복 기반 재귀 구조
    if n == 1: # 종료조건
        return x
    elif n % 2 == 0: # n이 짝수
        return power_dc(x * x, n//2) # 재귀 호출 절반크기로 감소
    else:
        return x * power_dc(x * x, (n - 1) // 2) # 재귀 호출 절반크기로 감소
    
x = 2.0
n = 10
print(f"억지 기법 _x 의 n 거듭 제곱 ({x}, {n} = {power_bf(x, n)})")
print(f"축소 기법 _x 의 n 거듭 제곱 ({x}, {n} = {power_dc(x, n)})")









