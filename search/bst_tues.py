# ==============================================================
# 이진 탐색 트리 (Binary Search Tree) 구현 + 성능 테스트
# ==============================================================
import random, time
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"  

# 1. 노드 클래스 정의
class bstnode:
    def __init__(self, key, value):
        #노드 생성 key(비교기준), value(저장 데이터), 좌우 자식은 None
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    #출력시 보기 좋은 형식으로 출력(튜플)
    def __repr__(self):
        return f"({self.key!r},{self.value!r})"        
    

# 2. 키(key)값으로 노드를 찾는 탐색 (순환구조)
def search_bst(n, key):
    # n : bstnode
    if n is not None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)



# 3. 값(value)으로 노드를 찾는 탐색 (전위 순회 기반)
def search_value_bst(n, value):
    if n is None:
        return None
    if value == n.value:
       return n
    res = search_value_bst(n.left, value)
    if res is None:
        return res
    else:
        search_value_bst(n.right, value)



# 4. 삽입 연산 (순환 구조)
def insert_bst(root, node):
    if root is None:
        return node
    if node.key == root.key:
        return root
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)

    return root
# 5. 삭제 연산
def delete_bst(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)

    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)

    return root


# 6. 순회 함수
def preorder(n): # n : BSTNode
    if n is not None:
        print(f'({n.key}:{n.value})', end=' ')
        preorder(n.left)
        preorder(n.right)

# 7. 출력 함수
def print_node(msg, n): # n: BSTNode
    if n is None:
        print(msg, "탐색 실패")
    else:
        print(msg, f"({n.key}:{n.value})")

def print_tree(msg, r): # r: 트리의 루트 노드
    print(msg, end='')
    preorder(r)
    print()

# 8. 기본 테스트　
if __name__ == "__main__":
    # 샘플 데이터: (key, value) 형식
    data = [
        (6, "여섯"),  # key=6
        (8, "여덟"),  # key=8
        (2, "둘"),    # key=2
        (4, "넷"),    # key=4
        (7, "일곱"),  # key=7
        (5, "다섯"),  # key=5
        (1, "하나"),  # key=1
        (9, "아홉"),  # key=9
        (3, "셋"),    # key=3
        (0, "영")     # key=0
    ]

    root = None # 루트를 초기화
    for key, value in data: # 각 항목으로 BSTNode 생성 후 트리에 삽입 (중복 키는 insert_bst에서 무시)
        root = insert_bst(root, bstnode(key, value))

    print_tree("현재 트리 전위순회:", root)

    # 키로 탐색
    n = search_bst(root, 3)
    print_node("srch 3:", n)

    n = search_bst(root, 8)
    print_node("srch 8:", n)

    n = search_bst(root, 0)
    print_node("srch 0:", n)

    n = search_bst(root, 10)
    print_node("srch 10:", n)

    # 값으로 탐색
    n = search_value_bst(root, "둘")
    print_node("search value '둘':", n)
    n = search_value_bst(root, "열")
    print_node("search value '열':", n)

    # 키 노드 삭제 후 전위순회 출력
    root = delete_bst(root, 7)
    print_tree("키=7 삭제 후 트리:", root)

    root = delete_bst(root, 8)
    print_tree("키=8 삭제 후 트리:", root)

    root = delete_bst(root, 2)
    print_tree("키=2 삭제 후 트리:", root)

    root = delete_bst(root, 6)
    print_tree("키=6 삭제 후 트리:", root)

# --------------------------------------------------------------
# 9. 성능 테스트 (삽입/탐색 속도)
# bst_perf_ｇｒａｐｈ＿test(sizes) 정의

# if __name__ == "__main__":
#     sizes = [1000, 2000, 5000, 10000, 20000]
#     # 그래프 시각화: bst_perf_ｇｒａｐｈ＿test 호출 후 결과 플롯
#     insert_times, search_times = bst_perf_ｇｒａｐｈ＿test(sizes)

#     plt.figure(figsize=(8,5))
#     plt.plot(sizes, insert_times, 'o-', color='seagreen', label='삽입 총시간 (ms)')
#     plt.plot(sizes, search_times, 'o-', color='orange', label='탐색 1회 평균 (ms)')
#     plt.title("BST 삽입/탐색 성능")
#     plt.xlabel("노드 수 (n)")
#     plt.ylabel("시간 (ms)")
#     plt.legend()
#     plt.grid(True, linestyle='--', alpha=0.6)
#     plt.tight_layout()
#     plt.show()
