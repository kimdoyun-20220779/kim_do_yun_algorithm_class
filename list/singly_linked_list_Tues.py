# singly_linked_list.py
#=========================================================
# 코드 3.1: 단순연결구조를 위한 Node 클래스
"""
1. 단순 연결 구조를 위한 Node 클래스
2. 각 노드는 데이터 필드(data)와 다음 노드를 가리키는 링크 필드(link)를 가짐
3. append(node): 현재 노드 뒤에 주어진 노드를 연결
4. popNext(): 현재 노드의 다음 노드를 리스트에서 제거하고, 그 노드를 반환
"""
# 단순연결구조를 위한 Node 클래스

class Node:
    def __init__(self, elem, link = None):
        self.data = elem # 데이터 필드
        self.link = link # 링크 필드
    
    def append(self, node):
        #노드와 노드 사이 삽입하는 연산
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):
        #다음 노드를 리스트에서 제거하고 반환
        next = self.link
        if next is not None:
            self.link = next.link
        return next



# 코드 3.2: 단순연결리스트 클래스
"""
1. 단순 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. 주요 메서드:
   - isEmpty(): 리스트가 비어있는지 확인
   - isFull(): 리스트가 가득 찼는지 확인
   - getNode(pos): 특정 위치의 노드를 반환
   - getEntry(pos): 특정 위치의 노드 데이터를 반환
   - replace(pos, elem): 특정 위치의 노드 데이터를 변경
   - size(): 리스트의 크기를 반환
   - display(msg): 리스트의 내용을 출력
   - insert(pos, elem): 특정 위치에 새 노드를 삽입
   - delete(pos): 특정 위치의 노드를 삭제
   - find(elem): 특정 데이터를 가진 노드를 검색
"""
# 단순연결리스트 클래스

class LinkedList:
    def __init__(self):
        self.head = None

    def isempty(self):
        # 리스트가 비어있는지 확인
        return self.head == None

    def isfull(self):
        # 리스트가 포화상태인지 확인
        return False

    def getNode(self, pos):
        # pos번에 있는 노드 반환
        if pos < 0 : return None
        if self.head == None:
            return None
        else:    
            ptr = self.head
            for _  in range(pos):
                if ptr == None:
                    return None
                ptr = ptr.link
            return ptr

    def getEntry(self, pos):
        # pos위치에 있는 노드의 데이터를 반환
        node = self.getNode(pos)
        if node == None : return None
        else:
            return node.data
        
    def insert(self, pos, elem):
        # pos 위치에 새로운 노드 추가
        if pos < 0 : return
        
        new = Node(elem)
        before = self.getNode(pos - 1)
        if before is None:
            if pos == 0: # 머리 노드로 삽입
                new.link = self.head
                self.head = new
            else: # pos가 리스트의 범위를 벗어남
                raise IndexError("리스트 밖에 있는 위치")
        else: #중간노드 삽입
            before.append(new) # before 노드에 삽입

    def delete(self, pos):
        # pos위치에 있는 노드 삭제
        if pos < 0 : raise IndexError("empty 혹은 범위 밖 오류")

        before = self.getNode(pos-1)

        if before is None:
            if pos == 0: # 머리노드 삭제 
                deleted = self.head
                self.head = deleted.link
                deleted.link = None
                return deleted
            else: # pos가 리스트 바깥 범위
                raise ValueError("리스트 밖에 있는 위치")
        else: 
            before.popNext() # 중간노드 삭제

    def size(self):
        if self.head == None : return 0 # 리스트가 빈 경우 0 반환
        ptr = self.head
        count = 0
        while ptr is not None:
            count+=1
            ptr = ptr.link
        return count
        
    def display(self, msg="Linkedlist"):
        print(msg, end = '     ')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '->')
            ptr = ptr.link
        print("None")

    def replace(self, pos, elem):
        # pos 위치에 있는 데이터 변경 106페이지 문제
        node = self.getNode(pos)

        if node is not None:
            node.data = elem
        else:
            return 



 
# 연습문제2: 어떤 요소를 찾아 위치를 반환하는 함수를 정의하기 : 리스트에 없으면 -1 반환, 있으면 그 위치를 정수로 반환

    
   
#=========================================================
# 테스트 프로그래램
#=========================================================
def test_code_3_3():
    #1. 연결 리스트 생성
    ll = LinkedList()
    ll.display("연결리스트(초기):   ")      # 출력: LinkedList: None

    #2. 노드 삽입
    ll.insert(0, 10) # 첫 번째 위치에 10 삽입
    ll.display("첫 번째 위치에 10 삽입")
    ll.insert(0, 20)  # 첫 번째 위치에 20 삽입
    ll.display("첫 번째 위치에 20 삽입")
    ll.insert(1, 30)  # 두 번째 위치에 30 삽입
    ll.display("두 번째 위치에 30 삽입")
    ll.insert(ll.size(), 40)  # 마지막 위치에 40 삽입
    ll.display("마지막 위치에 40 삽입")
    ll.insert(2, 50)  # 세 번째 위치에 50 삽입
    ll.display("세 번째 위치에 50 삽입")
    ll.display("연결리스트(삽입x5): ")     
    ll.replace(2,90) # 세 번째 위치의 노드 데이터를 90으로 변경
    ll.display("연결리스트(교체X1-> 90으로 변경): ")    

    # 3.노드 삭제
    ll.delete(2)      # 세 번째 노드 삭제
    ll.display("세 번째 노드 삭제")
    ll.delete(3)      # 네 번째 노드 삭제
    ll.display("네 번째 노드 삭제")
    ll.delete(0)      # 첫 번째 노드 삭제
    ll.display("첫 번째 노드 삭제")
    ll.display("연결리스트(삭제x3): "   )      

   


if __name__ == "__main__" :
    test_code_3_3()  
    # test()
    # quiz_2()


