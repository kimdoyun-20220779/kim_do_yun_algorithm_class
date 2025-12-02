# #1. Btruteforce algorithm : 문자열 매칭 문제

# def string_machting(text, pattern):
#     n = len(text) # 텍스트 길이
#     m = len(pattern) # 패턴 길이

#     for i in range(n - m + 1): # 텍스트의 각 위치에서 
#         j = 0 # 패턴의 시작 위치
#         while j < m and pattern[j] == text[i + j]: #패턴의 각 문자와 비교 O(m)
#             j += 1
#         if j == m: # 모든 패턴의 문자가 일치
#             return i # 일치하는 문자열의 시작 위치 반환
#     return -1


# #테스트 코드
# text = "HELLO WORLD"
# pattern = "LO"
# result = string_machting(text, pattern)

# if result != -1:
#     print(f"패턴이 텍스트에서 위치 {result} 에서 발견")
# else:
#     print("패턴이 텍스트에서 발견 되지 않음")

# #문자열 매칭문제 수정 : 전부 매칭 찾기

# def string_machting_all(text, pattern):
#     n = len(text) # 텍스트 길이
#     m = len(pattern) # 패턴 길이
#     matches = [] # 복수 개 매칭 위치 저장


#     for i in range(n - m + 1): # 텍스트의 각 위치에서 
#         j = 0 # 패턴의 시작 위치
#         while j < m and pattern[j] == text[i + j]: #패턴의 각 문자와 비교 O(m)
#             j += 1
#         if j == m: # 모든 패턴의 문자가 일치
#             matches.append(i) # 매칭 위치 저장
#     return matches


# #테스트 코드
# text = "ABABCABADAVSDACADGASJDASKAFOLAJSDILADIANABAJKABNAKLJANAKLS;JDASDJASIDHNASLKDASHNSDSADSAAB"
# pattern = "AB"
# result = string_machting_all(text, pattern)

# if result != -1:
#     print(f"패턴이 텍스트에서 위치 {result} 에서 발견")
# else:
#     print("패턴이 텍스트에서 발견 되지 않음")

# =================================================================================================
# 2. 0/1 배낭 채우기 문제
# =================================================================================================
# def knapsack01_bf(wgt, val, w):
#     """브루트 포스 방식으로 0/1 knapsack 문제 해결"""
#     # wgt : 물건 무게 리스트 val : val 무가 가치 리스트 w : 배낭 최대 무게

#     n = len(wgt) # 물건의 개수
#     bestval = 0 # 최대가치 초기화

#     bestset = [] # 최적조합 기록 
#     count = 0 # 부분집합 번호 표시용
    
#     for i in range(2**n): # 0~2^n - 1 모든 부분집합 조합 탐색
#         count += 1

#         # 1. 각조합에 대해 2진수 비트패턴 생성 => 리스트에 역순으로 저장
#         s = [0] * n

#         temp = i
#         for j in range(n):
#             s[j] = temp % 2 # j번째 비트 구하기
#             temp = temp // 2 # 다음 비트로 이동

#     print(f"{i} : i 조합의 비트 패턴(선택 여부): {s}")

#     #2. 현재 조합 (i)의 무게/가치 계산
#     sumwgt = 0 # 현재조합 i의 무게 합 
#     sumval = 0 # 현재조합 i의 가치 합
#     chosen_item = [] # 선택된 물건 인덱스 저장

#     for j in range(n):
#         sumwgt += wgt[j]
#         sumval += val[j]
#         chosen_item.append(j)

#         print("선택 물건 인덱스 : ", chosen_item, " / 총 무게 : ", sumwgt, " / 총 가치 : ", sumval)

#         # 3. 배낭 무게 조건 만족하면 최대값 갱신
#         if sumwgt <= w:
#             print("배낭 용량 충족")
#             if sumval > bestval:
#                 bestval = sumval # 최대 가치 갱신
#                 bestset = chosen_item[:] # 최적 조합 갱신
#                 print("-> 가치 최대값 갱신! 현재 최대 : ", bestval)
#             else:
#                 print("-> 가치 최대값 갱신 없음")
#         else:
#             print("배낭 용량 초과")
#     print()
#     return bestval, bestset

# weight = [10, 20, 30, 25, 35]
# value = [60, 100, 120, 70, 85]
# bestval, bestset = knapsack01_bf(weight, value, 80)
# print(f"최대가치 : {bestval} 최적조합 : {bestset}")


# =================================================================================================
# 알고리즘 설계 전략 : 탐욕적 기법
# =================================================================================================

# def coin_change_greedy(coins, amount):
#     #탐욕기법 정의 : 큰단위부터 사용하기 위해 정렬 = 액면각가 높은것부터 내림차순 절렬
#     coins.sort(reverse = True) # O(log n)

#     result = [] # (동전 단위, 사용개수) 저장
#     total_count = 0 # 총 동전 개수
#     remain = amount # 남은 금액

#     for coin in coins:
#         cnt = remain // coin
#         result.append((coin,cnt))
#         total_count += cnt
#         remain -= coin * cnt # 남은 갬액 갱신

#     if remain == 0:
#         return total_count, result # 사용된 동전 개수와 조합 반환
#     else:
#         return -1, [] # 정확이 만들수 없는 경우


# # coins = [500, 100, 50, 10, 5, 1]
# coins = [500, 60, 50, 10, 5, 1]

# amount = 620
# count, result = coin_change_greedy(coins, amount)
# if count != -1:
#     print(f"최소 동전 개수 : {count}")
#     print("사용된 동전 조합 : ", result)
# else:
#     print("조합 불가")

# =================================================================================================
# 2. 분할 가능한 배낭 문제
# =================================================================================================
# 정렬 + 배낭 채우기 문제
def knapsackfrac_greedy(wgt, val, w):
    # 반환 : (최대가치,가방에 채운 물건 기록)
    # item : (비율, 무게, 가치, 인덱스)

    n = len(wgt) # 물건의 개수

    # 단위 무게당 가격 비율 ratio 생성
    item = []
    for i in range(n):
        item.append((val[i] / wgt[i], wgt[i], val[i], i))

    # 단위 무게당 가격의 내림차순 정렬
    item.sort(reverse = True, key = lambda x : x[0])

    # greedy 채우기
    bestval = 0
    bag_with_item = [] # 가방에 채워지는 물품기록

    for ratio, wgi, vla, idx in item: # 비율이 높은 순서부터 물건 채워넣기
        if w <= 0: # 배낭이 채워진 경우
            break
        if w >= wgi: #물건을 통째로 넣을수 있는 경우
            w -= wgi # 넣은 후 남은 용량 갱신
            bestval += vla  # 최대 가치 증가
            bag_with_item.append(("full", idx, wgi, vla)) # 물건을 통째로 넣음
        else: # w < wgi 물건의 일부만 넣을수 있음
            fractiom = w / wgi
            bestval += vla * fractiom
            bag_with_item.append(("Part", idx, wgi, vla)) # 물건을 일부만 넣음
            w = 0 # 가방이 꽉참
            break

    return bestval, bag_with_item

wgt = [12, 10, 8]
val = [120, 80, 60]
w = 18

bestval, item = knapsackfrac_greedy(wgt, val, w)
print(f"테스트 밸류 : {bestval}, 테스트 아이템 {item}")