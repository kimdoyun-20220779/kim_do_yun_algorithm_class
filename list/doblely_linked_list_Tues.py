# doubly_linked_list.py
#=================================================================
# 코드 3.4 : 이중 연결 구조를 위한 Node 클래스 
"""
1. 이중 연결 구조를 위한 Node 클래스
2. 각 노드는 데이터 필드와 두 개의 링크 필드를 가짐
3. 링크 필드는 각각 이전 노드와 다음 노드를 가리킴
4. 이 구조는 양방향 탐색이 가능하게 함
5. 이중 연결 리스트의 기본 단위로 사용됨
6. 노드 생성 시 데이터와 링크 필드를 초기화
7. 주요 메서드:
    - append(node) : 새로운 노드를 현재 노드 뒤에 삽입
    - popNext() : 현재 노드 뒤에 있는 노드 삭제
"""


    
#===============================================================================================
# 코드 3.5: 이중연결리스트 클래스
"""
1. 이중 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. tail: 리스트의 마지막 노드를 가리키는 포인터(option)
4. 주요 메서드: 
    - 동일 연산
        - isEmpty(): 리스트가 비어있는지 확인 
        - isFull(): 리스트가 가득 찼는지 확인
        - getEntry(pos): 특정 위치의 노드 데이터를 반환
    - 연산에서 .link -> .next로 수정
        - getNode(pos): 특정 위치의 노드를 반환 
        - size(): 리스트의 크기를 반환
        - display(msg): 리스트의 내용을 출력
    - 나머지 연산       
        - insert(pos, elem): 특정 위치에 새 노드를 삽입
        - delete(pos): 특정 위치의 노드를 삭제
        - replace(pos, elem): 특정 위치의 노드 데이터를 변경
        - find(elem): 특정 데이터를 가진 노드를 검색
"""
class DLinkedList:                       
    def __init__( self ):             
      self.head = None                
    

    def isEmpty( self ):      
       return self.head == None       

    def isFull( self ):     
       return False                  
    
    def getEntry(self, pos) : 
        node = self.getNode(pos)      
        if node == None :              
            return None               
        else :                      
            return node.data         
    
    




#=========================================================
# 코드 3.3 단순연결리스트 테스트 프로그램 이용   
#1. 연결 리스트 생성
ll = DLinkedList()
ll.display("연결리스트(초기):   ")      # 출력: LinkedList: None

#2. 노드 삽입
ll.insert(0, 10) # 첫 번째 위치에 10 삽입
ll.insert(0, 20)  # 첫 번째 위치에 20 삽입
ll.insert(1, 30)  # 두 번째 위치에 30 삽입
ll.insert(ll.size(), 40)  # 마지막 위치에 40 삽입
ll.insert(2, 50)  # 세 번째 위치에 50 삽입
ll.display("연결리스트(삽입x5): ")     # 출력: LinkedList: 20->30->50->10->40->None 
ll.replace(2,90) # 세 번째 위치의 노드 데이터를 90으로 변경
ll.display("연결리스트(교체X1-> 90으로 변경): ")     # 출력: LinkedList: 20->30->90->10->40->None

# 3.노드 삭제
ll.delete(2)      # 세 번째 노드 삭제
ll.delete(3)      # 네 번째 노드 삭제
ll.delete(0)      # 첫 번째 노드 삭제
ll.display("연결리스트(삭제x3): "   )      # 출력: LinkedList: 30->10->None

print("연결리스트의 크기= ", ll.size())  # 출력: 연결리스트의 크기= 2
print("2번째 노드의 데이터= ", ll.getEntry(1)) # 출력: 2번째 노드의 데이터= 10
print("1번째 노드의 데이터= ", ll.getEntry(0)) # 출력: 1번째 노드의 데이터= 30
print("3번째 노드의 데이터= ", ll.getEntry(2)) # 출력: 3번째 노드의 데이터= None  


