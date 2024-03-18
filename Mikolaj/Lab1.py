class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
def check_valid_parenthesis(string):
    stack=Stack()
    for char in string:
        if stack.isEmpty():
            stack.push(char)
        elif char=="(":
            stack.push(char)
        else:
            stack.pop()
    if stack.isEmpty():
        return True
    else:
        return False
def weird_parenthesis(parentheses_string):
    stack = Stack()
    diction={"(":")",
             "[":"]",
             "{":"}"}
    for char in parentheses_string:
        if char in diction.keys():
            stack.push(char)
        elif not stack.isEmpty() and char==diction[stack.peek()]:
            stack.pop()
        else:
            return False
    return stack.isEmpty()
question1=['(()()())','((((()))))','(()(((())()))','(())(()))']
for strings in question1:
    print(check_valid_parenthesis(strings))
question2=['([]{}())','{([])[({()})}','(({}[{()}])]]','({}({([])()})']
for strings in question2:
    print(weird_parenthesis(strings))
