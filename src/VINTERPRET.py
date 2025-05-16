import sys

class SimpleLang:
    def __init__(self):
        self.vars = {}

    def run(self):
        print("Welcome to Conda REPL! Type 'exit;' to quit.")
        while True:
            try:
                line = input(">>> ").strip()
                if not line:
                    continue
                if line == 'exit;':
                    print("Goodbye!")
                    break
                self.parse(line)
            except Exception as e:
                print("Error:", e)

    def parse(self, line):
        # remove trailing semicolon if present
        if line.endswith(';'):
            line = line[:-1].strip()
        # tokenize line by spaces (super simple)
        tokens = line.split()
        if not tokens:
            return

        cmd = tokens[0]

        if cmd == "console.say":
            # syntax: console.say "Hello" OR console.say varName
            arg = line[len("console.say"):].strip()
            # remove quotes if string
            if arg.startswith('"') and arg.endswith('"'):
                print(arg[1:-1])
            else:
                # try variable print
                if arg in self.vars:
                    print(self.vars[arg])
                else:
                    raise NameError(f'Variable "{arg}" not defined')

        elif cmd == "set":
            # syntax: set varName = value
            if len(tokens) < 4 or tokens[2] != '=':
                raise SyntaxError("Usage: set varName = value")
            var = tokens[1]
            val = self.eval_expr(tokens[3])
            self.vars[var] = val

        elif cmd in ("add", "sub", "mul", "div"):
            # syntax: add varName value
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

        elif cmd == "input":
            # syntax: input varName
            if len(tokens) != 2:
                raise SyntaxError("Usage: input varName")
            var = tokens[1]
            val = input(f"Input for {var}: ")
            # try to convert to int or float if possible
            if val.isdigit():
                val = int(val)
            else:
                try:
                    val = float(val)
                except:
                    pass
            self.vars[var] = val

        elif cmd == "if":
            # syntax: if varName operator value then ... end
            # for simplicity, only support one-line if
            condition = line[len("if"):].strip()
            if "then" not in condition or "end" not in condition:
                raise SyntaxError("If syntax: if var op val then command end")
            cond_part = condition.split("then")[0].strip()
            then_part = condition.split("then")[1].split("end")[0].strip()

            # parse condition
            var_name, op, val = self.parse_condition(cond_part)
            if var_name not in self.vars:
                raise NameError(f'Variable "{var_name}" not defined')
            var_val = self.vars[var_name]
            val = self.eval_expr(val)

            if self.eval_condition(var_val, op, val):
                self.parse(then_part)

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
        # Try to convert val to int or float or else var lookup
        try:
            if '.' in val:
                return float(val)
            else:
                return int(val)
        except:
            # variable lookup
            if val in self.vars:
                return self.vars[val]
            else:
                raise NameError(f'Variable "{val}" not defined')

if __name__ == "__main__":
    SimpleLang().run()
