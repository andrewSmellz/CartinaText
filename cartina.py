import sys
import os

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
operation_count = 0
all_operations = ["push", "pop", "add", "sub", "mul", "div", "dupe", "swap", "top", "display", "print", "read", "==", ">", ">=", "<", "<=", "eqJump", "halt"]
operations = []
labels = {}  
lines = []

with open(ct_filepath, "r") as ct_program:
    for i, line in enumerate(ct_program.readlines()):
        program_lines.append(line.strip())
        tokens = line.strip().split()
        if tokens:
            op = tokens[0]
            if op in all_operations:
                operations.append(op)
                lines.append(i)  
            elif op[-1] == ":":
                labels[op[:-1]] = i  
                lines.append(i)  

i = 0  
while i < len(program_lines):
    line = program_lines[i].split()
    if line and line[0] == "~":
        i += 1
        continue
    tokens = program_lines[i].split()
    try:
        operation = tokens[0]
        match(operation):
            case "push":
                stack.push(float(tokens[1]))
            case "pop":
                stack.pop()
            case "add":
                a = stack.pop()
                b = stack.pop()
                stack.push(a + b)
            case "sub":
                a = stack.pop()
                b = stack.pop()
                stack.push(b - a)
            case "mul":
                a = stack.pop()
                b = stack.pop()
                stack.push(a * b)
            case "div":
                a = stack.pop()
                b = stack.pop()
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
                print(stack.top())
            case "display":
                stack.display()
            case "print":
                message = " ".join(tokens[1:])
                message = message[1:-1]
                print(message)
            case "read":
                x = float(input())
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
                if stack.top() == 1:
                    label = tokens[1]
                    if label in labels:
                        i = labels[label] 
                        continue  
            case "halt":
                break
        i += 1  
    except:
        i += 1
