# CartinaText
## welcome to a silly little programming language
### a turing complete stack based programming language
**file extension is .ct**

**to execute code run the following in terminal**
`python cartina.py example.ct`
Replace `example.ct` with the name of your CartinaText program.

Currently, CartinaText does not support multiple operations in one line (e.g., `print pop` will not pop a value and instead will print "pop").

### Syntax
Refer to the example program (`example.ct`) for examples of the syntax.

Lines beginning with `~` are comments. Currently, there is no support for inline comments.

### Commands

#### Stack Operations
- **push**: Adds a value to the top of the stack.  
  Example: `push 5`
- **pop**: Removes the value from the top of the stack.  
  Example: `pop`
- **add**: Pops the top two values, adds them, and pushes the result.  
  Example: `add`
- **sub**: Pops the top two values, subtracts the second from the first, and pushes the result.  
  Example: `sub`
- **mul**: Pops the top two values, multiplies them, and pushes the result.  
  Example: `mul`
- **div**: Pops the top two values, divides the second by the first, and pushes the result.  
  Example: `div`
- **dupe**: Duplicates the top value on the stack.  
  Example: `dupe`
- **swap**: Swaps the top two values on the stack.  
  Example: `swap`
- **display**: Prints all values on the stack.  
  Example: `display`
- **top**: Prints the top value of the stack without popping it.  
  Example: `top`

#### I/O Operations
- **print**: Prints a string literal to the terminal (string should be enclosed in quotes).  
  Example: `print "hello world"`
- **read**: Reads user input and pushes it to the stack.  
  Example: `read`

#### Comparison Operations
- **==**: Compares the top two values for equality; pushes 1 if equal, 0 otherwise.  
  Example: `==`
- **>**: Compares if the second value is greater than the top value; pushes 1 if true, 0 otherwise.  
  Example: `>`
- **<**: Compares if the second value is less than the top value; pushes 1 if true, 0 otherwise.  
  Example: `<`
- **>=**: Checks if the second value is greater than or equal to the top value; pushes 1 if true, 0 otherwise.  
  Example: `>=`
- **<=**: Checks if the second value is less than or equal to the top value; pushes 1 if true, 0 otherwise.  
  Example: `<=`

#### Control Flow
- **eqJump**: If the top value is 1, jumps to the specified label.  
  Example: `eqJump lbl`
- **neqJump**: If the top value is 0, jumps to the specified label.  
  Example: `neqJump lbl`
- **halt**: Halts program execution.  
  Example: `halt`

#### Variables and Arrays
- **var**: Declares a variable.  
  Example: `var x`
- **setVar**: Sets a variable to the top stack value.  
  Example: `setVar x`
- **getVar**: Prints the value of a variable.  
  Example: `getVar x`
- **pushVar**: Pushes the value of a variable onto the stack.  
  Example: `pushVar x`
- **arr**: Declares an array.  
  Example: `arr myArray`
- **arr.append**: Appends the value at the top of the stack to the array.  
  Example: `arr.append myArray`
- **getArr**: Prints all values in an array.  
  Example: `getArr myArray`

#### String Operations
- **string**: Declares a string in an array format.  
  Example: `string greeting "Hello, World!"`
- **getStr**: Prints the string stored in an array.  
  Example: `getStr greeting`
