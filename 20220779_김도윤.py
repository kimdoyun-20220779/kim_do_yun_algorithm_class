
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year  
        
    def __str__(self):
        return (f"책 번호: {self.book_id}, 책 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}")
class Node:
    def __init__(self, elem, next = None):
        self.data = elem # 데이터 필드
        self.link = next # 링크 필드
    
    def append(self, new):
        #노드와 노드 사이 삽입하는 연산
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        #다음 노드를 리스트에서 제거하고 반환
        next = self.link
        if next is not None:
            self.link = next.link
        return next




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
        print(msg)
        print("-----------------------------------------------------")
        ptr = self.head
        if ptr is None:
            print("[실패] 현재 등록된 도서가 없습니다. 조회 작업을 진행할 수 없습니다.")
            return

        while ptr is not None:
            print(ptr.data) 
            ptr = ptr.link
        print("-----------------------------------------------------")

class BookMangement:
    def __init__(self):
        self.library = LinkedList() 

    def add_book(self, book_id, title, author, year):
        ptr = self.library.head
        while ptr is not None:
            if ptr.data.title == title: # 책 제목 중복 검사
                print(f"[실패] 책제목 : {title}도서가 이미 등록되어 있습니다.")
                return
            if ptr.data.book_id == book_id: # 책 번호 중복 검사
                print(f"[실패] 책 번호 : {book_id}는 이미 사용 중입니다.")
                return
            ptr = ptr.link

        # 맨 끝에 도서 추가
        new_book = Book(book_id, title, author, year)
        self.library.insert(self.library.size(), new_book)
        return True, f"도서 '{title}'이(가) 성공적으로 추가되었습니다."
    
    def remove_book(self, title):
        pos = -1  
        current = self.library.head
                
        # 제목으로 위치(pos) 찾기
        for i in range(self.library.size()):
            if current.data.title == title:
                pos = i
                break
            current = current.link

        if pos == -1:
            print(f"\n[실패] 책제목 : {title}의 도서를 찾을 수 없어 삭제에 실패했습니다.")
            return

        # 해당 위치의 노드 삭제
        deleted_node = self.library.delete(pos)
        
        if deleted_node:
            print(f"\n[성공] 책제목 : {title}의 도서가 성공적으로 삭제되었습니다.")
    
    def search_book(self, title):
        current = self.library.head
        found_book = None
                
        # 제목으로 도서 찾기
        while current is not None:
            if current.data.title == title:
                found_book = current.data
                break
            current = current.link

        # 결과 출력
        if found_book is not None:
            print("\n[조회 성공]")
            print("-----------------------------------------------------")
            print(found_book) 
            print("-----------------------------------------------------\n")
        else:
            print(f"\n[조회 실패] 책제목 : {title}의 도서를 찾을 수 없습니다.")
    def display_books(self):
        self.library.display("전체 도서 목록")


def run():

    BM = BookMangement()

    while(True):
        print("===도서 관리 프로그램===\n")
        print("1. 도서 추가 \n")
        print("2. 도서 삭제 (책 제목으로 삭제) \n")
        print("3. 도서 조회 (책 제목으로 조회) \n")
        print("4. 전체 도서 목록 출력 \n")    
        print("5. 종료 \n")    
        select = input("메뉴를 선택하세요 : ")
    
        if select == '5':
            break
        elif select == '1':
            book_id = input("책 번호를 입력하세요\n").strip()
            title = input("책 이름을 입력하세요 \n") .strip()
            author = input("책 저자를 입력하세요 \n").strip()
            year = input("출판 연도를 입력하세요 \n").strip()
            if not book_id or not title or not author or not year:
                print("[실패] 모든 필드를 입력해야 합니다.")
                continue
            if not book_id.isdigit(): # 책 번호 필수/숫자 검사
                print("[실패] 책 번호는 숫자로만 구성되어야 합니다.")
                continue
            if any(char.isdigit() for char in author):# 저자 이름 필수/숫자 포함 검사
                print("[실패] 저자 이름에 숫자가 포함될 수 없습니다.")
                continue
            if not year.isdigit(): # 출판 연도 숫자 검사 
                print("[실패] 출판 연도는 숫자로만 구성되어야 합니다.")
                continue
                    
            BM.add_book(book_id, title, author, year)
        elif select == '2':
            if BM.library.isempty(): # 리스트 비어있는 경우 체크
                print("\n[실패] 현재 등록된 도서가 없습니다. 삭제 작업을 진행할 수 없습니다.")
                continue

            print("\n[도서 삭제]")
            title = input("삭제할 도서의 책 제목을 입력하세요: ").strip()
            if not title:
                print("[실패] 책 제목을 입력해야 삭제할 수 있습니다.")
                continue
            BM.remove_book(title)
                
        elif select == '3':
            if BM.library.isempty(): # 리스트 비어있는 경우 체크
                print("\n[실패] 현재 등록된 도서가 없습니다. 조회 작업을 진행할 수 없습니다.")
                continue
            print("\n[도서 조회]")
            title = input("조회할 도서의 책 제목을 입력하세요: ").strip()
            if not title:
                print("[실패] 책 제목을 입력해야 조회할 수 있습니다.")
                continue
            BM.search_book(title)
                
        elif select == '4':
            print("\n[전체 도서 목록]")
            BM.display_books()
                

        else:
            print("1 ~ 5중에 선택해주세요 \n")
        

if __name__ == "__main__" :
    run()  








