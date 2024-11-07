import sys

class stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return len(self.items)==0
    
    def display(self):
        print(self.items)

ct_filepath=sys.argv[1]
program_lines=[]

stack = stack()

with open(ct_filepath,"r") as ct_program:
    for line in ct_program.readlines():
        program_lines.append(line.strip())

for instruction in program_lines:
    tokens=(instruction.split())
    operation = tokens[0]

    match(operation):
        case "push":
            stack.push(float(tokens[1]))
        case "pop":
            stack.pop()
        case "add":
            a=stack.pop()
            b=stack.pop()
            stack.push(a+b)
        case "sub":
            a=stack.pop()
            b=stack.pop()
            stack.push(b-a)
        case "top":
            stack.top()
        case "display":
            stack.display()
        case "print":
            print(*tokens[1:])
        case "read":
            x=float(input())
            stack.push(x)
            
