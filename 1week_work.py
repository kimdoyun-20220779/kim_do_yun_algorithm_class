# Stack 클래스 정의
class arrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.array[self.top] = item
            print(f"PUSH : {item!r} -> stack is now {self.array[:self.top+1]}")
        else:
            raise OverflowError("Stack Overflow")
        
    def pop(self):
        if not self.is_empty(): 
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            print(f"POP : {item!r} -> stack is now {self.array[:self.top+1]}")
            return item
        else:
            raise IndexError("Stack Underflow") 

    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None

    def size(self):
        return self.top + 1

# 문자열 뒤집기 함수
def reverse_string(statement):
    print("\n[1] Push 단계 -------------------------------------")
    stack = arrayStack(len(statement))
    for char in statement:
        stack.push(char)
    
    print("\n[2] Pop 단계 -------------------------------------")
    out = []
    while not stack.is_empty():
        out.append(stack.pop())
    
    result = ''.join(out)
    print(f"\n[3] 최종 결과 : {result}")
    return result

# 프로그램 실행 부분
if __name__ == "__main__":
    x = input("원하는 단어 입력: ")
    reverse_string(x)  # 함수 호출
