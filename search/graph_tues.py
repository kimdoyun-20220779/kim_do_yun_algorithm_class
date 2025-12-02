#===========================================
# Graph 관련 알고리즘
#===========================================
# 1. 깊이 우선 탐색 (DFS) - 인접행렬 기반 재귀 구현
def DFS(vtx, adj, s, visited):
    print(vtx[s], end= ' ')
    visited[s] = True
    
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                DFS(vtx, adj, v, visited)

# -------------------------------
# 테스트 코드
# -------------------------------
# if __name__ == "__main__":
#     # 정점 리스트
#     vtx = ['U', 'V', 'W', 'X', 'Y']

#     # 인접 행렬 
#     edge= [
#         [0,1,1,0,0],    # U -> V, W
#         [1,0,1,1,0],    # V -> U, W, X
#         [1,1,0,0,1],    # W -> U, V, Y
#         [0,1,0,0,0],    # X -> V
#         [0,0,1,0,0]     # Y -> W
#     ]
        

#     print('DFS(출발: U) : ', end="")
#     visited = [False] * len(vtx)   # 방문 여부 리스트 초기화
#     DFS(vtx, edge, 0, visited)     # U(인덱스 0)에서 시작


# 2. 너비 우선 탐색 (BFS) - 인접 리스트 사용
 
from collections import deque # FIFO 큐 파이썬 모듈
def BFS_AL(vtx, alist, s):
    n = len(vtx) # 정점의 개수
    visited = [False]*n # 방문 여부 기록 리스트
    q = deque() # 큐 생성
    q.append(s) # 시작 정점을 큐에 삽입
    visited[s] = True # 방문 표시

    while q: # 큐가 빌때까지
        s = q.popleft() # 큐의 맨 앞 정점 꺼내기
        print(vtx[s], end = ' ') # 방문 정점 출력
        
        #s의 인접 정점들 순회
        for v in alist[s]:
            if not visited[v]:
                q.append(v) # 방문하지 않은 정점 큐에 삽입
                visited[v] = True # 방문 표시


# -------------------------------
# 테스트 코드
# -------------------------------
if __name__ == "__main__":
    # 정점 리스트
    vtx = ['U', 'V', 'W', 'X', 'Y']
    # 인접 리스트 
    alist = [
        [1, 2],     # U -> V, W
        [0, 2, 3],  # V -> U, W, X
        [0, 1, 4],  # W -> U, V, Y
        [1],        # X -> V
        [2]         # Y -> W
    ]
    

    print('BFS_AL(출발: U) : ', end="")
    BFS_AL(vtx, alist, 0)  # 시작점 U는 인덱스 0



# 3. DFS를 이용한 신장트리 생성 (인접행렬 방식)



# -------------------------------
# 테스트 코드
# -------------------------------
# if __name__ == "__main__":
#     # 정점 리스트
    
#     # 인접 행렬 
    

#     print("ST_DFS_AM : ", end="")
#     visited = [False] * len(vtx)
#     ST_DFS(vtx, adj, 0, visited)   # U에서 시작


# 4. Prim 알고리즘 (인접행렬 방식)
# getMinVertex()를 내부 함수로 정의
# INF = 999 => 간선이 없음을 의미

def MSTPrim(vertex, adj, INF = 999):
    n = len(vertex)
    dist = [INF] * n # 각 정점까지의 최소 거리
    selected = [False] * n # MST의 정점 포함 여부 기록
    dist[0] = 0 # 시작 정점의 거리 = 0

    def getMinVertex(dist, selected):
        # MST에 포함되지 않은 정점 중 최소 dist를 가진 정점을 반환
        # 매번 전체 정점을 선형탐색 찾기
        minv = -1
        mindist = INF
        for v in range(len(dist)):
            if not selected[v] and dist[v] < mindist:
                mindist = dist[v]
                minv = v
        return minv
    
    print("정점 추가 순서 : ", end = ' ')
    print()
    for _ in range(n):
        u = getMinVertex(dist, selected)
        
        selected[u] = True
        print(vertex[u], "(", dist[u],")", end= ' ' ) # MST에 추가된 정점 출력

        #거리 갱신 : 그 정점과 연결된 간선으로 다른 정들의 거리 갱신

        for v in range(n):
            if adj[u][v] != INF and not selected[v]:
                if adj[u][v] < dist[v]:
                    dist[v] = adj[u][v] 
            print("|", vertex[u], "-", vertex[v],"=>", dist[v], end= ' ' )    

        print(": ", dist) # 중간 dist 출력

    print("\n최종 dist 배열", dist)
    print(" MST 총 비용 ", sum(dist))

# ---------------------------------------------------
# 테스트 코드
# ---------------------------------------------------
if __name__ == "__main__":
    # 정점 리스트
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # 인접 가중치 행렬 
    adj = [
        # A   B    C    D    E    F    G
        [ 0,  25, 999, 12, 999, 999, 999],  # A
        [25,   0, 10, 999, 15, 999, 999],   # B
        [999, 10,  0, 999, 999, 16, 999],   # C
        [12, 999, 999, 0, 17, 999, 37],     # D
        [999, 15, 999, 17, 0, 14, 19],      # E
        [999, 999, 16, 999, 14, 0, 42],     # F
        [999, 999, 999, 37, 19, 42, 0]      # G
    ]

    MSTPrim(vertex, adj)

