## Konda V1.0.1🗻
<p align="center">
  <img src="assets/logo.png.png" alt="Konda Logo" width="450"/>
</p>


 Derived from the Telugu word "Konda" "కొండ" meaning huge big mountains. Konda is a simple, beginner-friendly interpreted language designed for quick scripting, It helps bulding basic coding mindset and fundamentals so that you can learn more langauges in future!.  
It supports basic variable management, arithmetic operations, input handling, conditional execution, and console output. I have putten the new version changelog in the interpreter itself.

Built for simplicity and ease of use, Konda offers a minimal yet powerful command set ideal for educational projects and rapid prototyping.
I have built the Konda Interpreter from scratch. Libs used- sys

---

## Supported Commands

- `console.say` — Print text or variables  
- `set` — Assign values to variables  
- `add`, `sub`, `mul`, `div` — Arithmetic operations on variables    
- `if ... then ... end` — Conditional execution
- `console.input`- Takes input for a variable. For eg `console.input varName "message"`
- `func ... end`- Defines a function. End is used to end the function. Eg syntax `func greet`
- `run` - Runs a function
- `console.funcs` - Prints all defined functions   
- `console.vars` - Prints all defined variables                              

---

⚠️ **Note:** Konda is currently under development. More features and improvements are coming soon!

---

🚀 Konda is **fully open source**! Feel free to explore, contribute, and make it better.

---

Start experimenting with Konda today for a straightforward and fun coding experience!

---

## Example Session!

```plaintext
Welcome to Konda REPL! Type 'exit;' to quit.
>>> set x = 10
>>> set y = 5
>>> add x 3
>>> sub y 2
>>> mul x 2
>>> div y 1
>>> console.say "Values after math operations:"
Values after math operations:
>>> console.vars
Variables: {'x': 26, 'y': 3}
>>> func greet
>>>     console.say "Hello from function!"
>>> end
>>> run greet
Hello from function!
>>> console.input name "Enter your name"
Enter your name: Vihaan
>>> console.say name
Vihaan
>>> if x >= 20 then console.say "x is big!" end
x is big!
>>> console.clear
[clears screen]
>>> exit
Goodbye!

