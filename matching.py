def matching():
    brackets={'(': ')', '[': ']', '{': '}'}
    with open("main.py", "r") as f:
        lines = f.readlines()
    
    for line in lines:
        stack=[]
        for c in line:
            if c in ['(', '[', ')', '{',']','}']:
                stack.append(c)
            
        while stack:
            if stack[0] in brackets.keys() and brackets[stack[0]]==stack[-1]:
                stack.pop()
                stack.pop(0)
            else:
                print(f"Error in line {lines.index(line)+1}")
                return False
    return True
                
matching()
        