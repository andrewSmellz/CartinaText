# CartinaText
## welcome to a silly little programming language
### a turing complete stack based programming language
**file extension is .ct**

**to execute code run the following in terminal**
`python cartina.py example.ct`    replace example.ct with name of CartinaText program you are interpreting

currently no support for multiple operations in 1 line
ie `print pop` will not pop a value and will instead print "pop"


### syntax
refer to example program for visualization of syntax

lines beginning with `~` are commented out 
currently no inline comments
* **push** 
    add a value to top of stack
    `push 5`
* **pop**
    remove value from top of stack
    `pop`
* **add**
    pops and adds top two values on stack
    `add`
* **sub**
    pops and subtracts top two values on stack
    `sub`
* **top**
    access top value on stack without altering it
    `top`
* **display**
    print all values on stack to terminal
    `display`
* **print**
    print a string literal to the terminal
    `print hello world`
* **read**
    read a user input from the terminal
    `read`
* **==**
    compare top two values on stack for equality, if equal push 1, else push 0
    `==`
* **>**
    compare top two values on stack for greater than, if greater push 1, else push 0
    `>`
* **<**
    compare top two values on stack for less than, if less than push 1, else push 0
    `<`
* **>=**
    compare top two values on stack for equality or greater, if equal or greater push 1, else push 0
    `>=`
* **<=**
    compare top two values on stack for equality or less, if equal or less push 1, else push 0
    `<=`
* **eqJump**
    checks if top value of stack is 1, if so jumps to specificied label
    `eqJump lbl`
* **halt**
    halts program execution
    `halt`
