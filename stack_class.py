# 괄호 검사 프로그램
from stack_class import ArrayStack

def checkBrackets(statement):
    #여는 괄호는 push, 담는 괄호가 나오면 스택의 맨 위와 짝이 맞는지 확인 후 pop -> LTFO 이용

    pairs = {')':'(','[':']','}':'{'}
    openings = set(pairs.values())
    stack = Arraystack(len(statement))

    for ch in statement: # 입력 문자열 순회
        if ch in openings: #여는 괄호이면 스텍이 push
                stack.push(ch)
        elif ch in pairs: #닫힌 괄호이면 
             if stack.is_empty() : # 조건 2 위반 : 짝이 맞지 않음
                return false
             if stack.peek()  != pairs[ch] : #조건 3위반 : 짝이 맞지 않음
                return false
                stack.pop()
    else:
            pass # 괄히 아니면 무시

    return stack.is_empty() # True -> 검사 성공 , False: 조건 1 위반 (여는 괄히가 남아있음)

#테스트 하기
def test_brackets():
    test = [
        "{A[(i+1)=0;]}", # True}
        "if ((x<0)) && (y<3)", # False
        'WHILE  (N<8)) {N++}', 
        "arr[(i+1)]=0", # False
    ]
            
    for t in tests:
        print(t, "->", checkBrackets(t))

if __name__ == "__main__":
    test_brackets()
    
