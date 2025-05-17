import sys
import os

class KondaInterpreter:
    def __init__(self):
        self.vars = {}
        self.funcs = {}
        self.in_func_def = False
        self.current_func_name = ""
        self.current_func_lines = []

    def show_changelog_once(self):
        flag_file = os.path.expanduser("~/.konda_seen")
        if not os.path.exists(flag_file):
            print("📜 Changelog v1.0.1")
            print("- Added new command system ")
            print("- Function definitions supported ")
            print("- Basic arithmetic & input/output ")
            print("- If-statement logic implemented ")
            print("- Type 'console.funcs' or 'console.vars' to see all listed variables and functions! \n")
            with open(flag_file, "w") as f:
                f.write("changelog_shown=true")

    def run(self):
        self.show_changelog_once()
        print("Welcome to Konda REPL! Type 'exit' to quit.")
        while True:
            try:
                line = input(">>> ").strip()
                if line == "":
                    continue
                if line.lower() == "exit":
                    print("Goodbye!")
                    break
                self.handle_line(line)
            except Exception as e:
                print("Error:", e)

    def handle_line(self, line):
        if self.in_func_def:
            if line == "end":
                self.funcs[self.current_func_name] = self.current_func_lines.copy()
                self.in_func_def = False
                self.current_func_name = ""
                self.current_func_lines = []
            else:
                self.current_func_lines.append(line)
            return

        if line.startswith("func "):
            self.in_func_def = True
            self.current_func_name = line.split()[1]
            self.current_func_lines = []
        elif line.startswith("run "):
            name = line.split()[1]
            if name in self.funcs:
                for cmd in self.funcs[name]:
                    self.handle_line(cmd)
            else:
                raise NameError(f"Function '{name}' not found")
        else:
            self.parse(line)

    def parse(self, line):
        tokens = line.split()
        if not tokens:
            return

        cmd = tokens[0]

        if cmd == "console.say":
            arg = line[len("console.say"):].strip()
            if arg.startswith('"') and arg.endswith('"'):
                print(arg[1:-1])
            else:
                if arg in self.vars:
                    print(self.vars[arg])
                else:
                    raise NameError(f'Variable "{arg}" not defined')

        elif cmd == "console.input":
            if len(tokens) < 3:
                raise SyntaxError("Usage: console.input varName \"message\"")
            var = tokens[1]
            msg_start = line.find('"')
            if msg_start == -1 or not line.endswith('"'):
                raise SyntaxError("Input message must be in quotes")
            msg = line[msg_start+1:-1]
            val = input(msg + " ")
            try:
                val = int(val)
            except:
                try:
                    val = float(val)
                except:
                    pass
            self.vars[var] = val

        elif cmd == "console.clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif cmd == "console.vars":
            print("Variables:", self.vars)

        elif cmd == "console.funcs":
            print("Functions:", list(self.funcs.keys()))

        elif cmd == "set":
            if len(tokens) < 4 or tokens[2] != '=':
                raise SyntaxError("Usage: set varName = value")
            var = tokens[1]
            val = self.eval_expr(tokens[3])
            self.vars[var] = val

        elif cmd in ("add", "sub", "mul", "div"):
            if len(tokens) < 3:
                raise SyntaxError(f"Usage: {cmd} varName value")
            var = tokens[1]
            if var not in self.vars:
                raise NameError(f'Variable "{var}" not defined')
            val = self.eval_expr(tokens[2])
            if cmd == "add":
                self.vars[var] += val
            elif cmd == "sub":
                self.vars[var] -= val
            elif cmd == "mul":
                self.vars[var] *= val
            elif cmd == "div":
                if val == 0:
                    raise ZeroDivisionError("Division by zero")
                self.vars[var] /= val

        elif cmd == "if":
            condition = line[len("if"):].strip()
            if "then" not in condition or "end" not in condition:
                raise SyntaxError("If syntax: if var op val then command end")
            cond_part = condition.split("then")[0].strip()
            then_part = condition.split("then")[1].split("end")[0].strip()

            var_name, op, val = self.parse_condition(cond_part)
            if var_name not in self.vars:
                raise NameError(f'Variable "{var_name}" not defined')
            var_val = self.vars[var_name]
            val = self.eval_expr(val)

            if self.eval_condition(var_val, op, val):
                self.handle_line(then_part)

        else:
            raise SyntaxError(f"Unknown command: {cmd}")

    def parse_condition(self, cond):
        for op in ['==', '!=', '>=', '<=', '>', '<']:
            if op in cond:
                parts = cond.split(op)
                if len(parts) != 2:
                    raise SyntaxError("Invalid condition")
                return parts[0].strip(), op, parts[1].strip()
        raise SyntaxError("Invalid operator in condition")

    def eval_condition(self, var_val, op, val):
        if op == "==":
            return var_val == val
        elif op == "!=":
            return var_val != val
        elif op == ">":
            return var_val > val
        elif op == "<":
            return var_val < val
        elif op == ">=":
            return var_val >= val
        elif op == "<=":
            return var_val <= val
        else:
            raise SyntaxError("Unknown operator")

    def eval_expr(self, val):
        try:
            if '.' in val:
                return float(val)
            else:
                return int(val)
        except:
            if val in self.vars:
                return self.vars[val]
            else:
                raise NameError(f'Variable "{val}" not defined')


if __name__ == "__main__":
    KondaInterpreter().run()
