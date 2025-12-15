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
