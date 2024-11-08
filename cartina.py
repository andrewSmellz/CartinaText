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
        return len(self.items) == 0
    
    def display(self):
        print(self.items)

ct_filepath = sys.argv[1] 

program_lines = []
stack = stack()
labels = {}  
variables = {}
arrays = {}
i = 0

# Read and parse the program lines
with open(ct_filepath, "r") as ct_program:
    for i, line in enumerate(ct_program.readlines()):
        line = line.strip()
        program_lines.append(line)
        if line.endswith(":"):
            labels[line[:-1]] = i

# Execute the program
i = 0
while i < len(program_lines):
    line = program_lines[i].split()
    if line and line[0] == "~":
        i += 1
        continue

    tokens = program_lines[i].split()

    while tokens:
        operation = tokens.pop(0)  
        match operation:
            case "push":
                stack.push(tokens.pop(0))
            case "pop":
                stack.pop()
            case "add":
                a = float(stack.pop())
                b = float(stack.pop())
                stack.push(a + b)
            case "top":
                print(stack.top())
            case "sub":
                a = float(stack.pop())
                b = float(stack.pop())
                stack.push(b - a)
            case "mul":
                a = float(stack.pop())
                b = float(stack.pop())
                stack.push(a * b)
            case "div":
                a = float(stack.pop())
                b = float(stack.pop())
                if a != 0:
                    stack.push(b / a)
                else:
                    print("Error: Division by zero")
                    stack.push(0)
            case "dupe":
                top = stack.top()
                stack.push(top)
            case "swap":
                a = stack.pop()
                b = stack.pop()
                stack.push(a)
                stack.push(b)
            case "top":
                stack.top()
            case "display":
                stack.display()
            case "print":
                message = []
                running=True
                while running:
                    if tokens[0].startswith('"'):
                        tokens[0]=tokens[0][1:]
                    if tokens[0].endswith('"'):
                        tokens[0]=tokens[0][:-1]
                        running=False
                    message.append(tokens.pop(0))
                print(" ".join(message))
            case "read":
                x = input()
                stack.push(x)
            case "==":
                a = stack.pop()
                b = stack.pop()
                if a == b:
                    stack.push(1)
                else:
                    stack.push(0)
            case ">":
                a = stack.pop()
                b = stack.pop()
                if a > b:
                    stack.push(1)
                else:
                    stack.push(0)
            case "<":
                a = stack.pop()
                b = stack.pop()
                if a < b:
                    stack.push(1)
                else:
                    stack.push(0)
            case ">=":
                a = stack.pop()
                b = stack.pop()
                if a >= b:
                    stack.push(1)
                else:
                    stack.push(0)
            case "<=":
                a = stack.pop()
                b = stack.pop()
                if a <= b:
                    stack.push(1)
                else:
                    stack.push(0)
            case "eqJump":
                if int(stack.top()) == 1:
                    label = tokens.pop(0)
                    if label in labels:
                        i = labels[label]  
                        continue
            case "neqJump":
                if stack.top() == 0:
                    label = tokens.pop(0)
                    if label in labels:
                        i = labels[label]
                        continue
            case "halt":
                break
            case "var":
                variables[tokens.pop(0)]=None
            case "setVar":
                variables[tokens.pop(0)]=stack.pop()
            case "getVar":
                print(variables[tokens.pop(0)])
            case "pushVar":
                stack.push(variables[stack.pop()])
            case "arr":
                arrays[tokens.pop(0)]=[]
            case "arr.append":
                arr=tokens.pop(0)
                arrays[arr].append(tokens.pop(0))
            case "getArr":
                arr=tokens.pop(0)
                z=0
                for z in range(len(arrays[arr])):
                    print(arrays[arr][z], end=" ")
                    z+=1
                print()
            case "string":
                arr=tokens.pop(0)
                message = []
                running=True
                while running:
                    if tokens[0].startswith('"'):
                        tokens[0]=tokens[0][1:]
                    if tokens[0].endswith('"'):
                        tokens[0]=tokens[0][:-1]
                        running=False
                    message.append(tokens.pop(0))
                arrays[arr]=[" ".join(message)]
            case "getStr":
                arr=tokens.pop(0)
                z=0
                for z in range(len(arrays[arr])):
                    print(arrays[arr][z], end="")
                    z+=1
                print()
            
    i += 1  
