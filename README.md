# Konda
<p align="center">
  <img src="assets/logo.png.png" alt="Konda Logo" width="250"/>
</p>


Konda is a simple, beginner-friendly interpreted language designed for quick scripting and learning programming fundamentals.  
It supports basic variable management, arithmetic operations, input handling, conditional execution, and console output.

Built for simplicity and ease of use, Konda offers a minimal yet powerful command set ideal for educational projects and rapid prototyping.
I have built the Konda Interpreter from scratch. Libs used- sys

---

## Supported Commands

- `console.say` — Print text or variables  
- `set` — Assign values to variables  
- `add`, `sub`, `mul`, `div` — Arithmetic operations on variables  
- `input` — Read user input  
- `if ... then ... end` — Conditional execution  

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
>>> console.say "Hello world!"
Hello world!
>>> set x = 10
>>> console.say x
10
>>> add x 5
>>> console.say x
15
>>> sub x 3
>>> console.say x
12
>>> mul x 2
>>> console.say x
24
>>> div x 4
>>> console.say x
6.0
>>> input y
Input for y: 20
>>> console.say y
20
>>> if x > 5 then console.say "x is greater than 5" end
x is greater than 5
>>> if y == 20 then console.say x end
6.0
>>> if y != 10 then add x 10 end
>>> console.say x
16.0
>>> exit;
Goodbye!
