import math
history =[]
def show_help():
    print(""" ---- Commands ---
          Type any of this:
            help
            history
            save
            mode
            quit
          --------------------""")
def show_history():
    if not history:
        print("No history yet")
    else:
        print("\n---History ---")
        for entry in history:
            print(entry)
        print("---------------/n")
def save_history(filename="calc_history.txt"):
    with open(filename,"w")as f:
        for entry in history:
            f.write(entry+"\n")
    print(f"History saved to {filename}")
def basic_calc(): 
    try:
        num1 = float(input("Enter first number:"))
        op = input("Enter operator(+,-,*,/): ").strip()
        num2 = float(input("Enter second number: "))
        if op=='+':
            result=num1+num2
        elif op=='-':
            result=num1-num2
        elif op=='*':
            result=num1*num2
        elif op=='/':
            result=num1/num2 if num2 != 0 else "Error: Divide by zero"
        else:
            return "Invalid operator"
        history.append(f"{num1} {op} {num2} = {result}")
        return result
    except Exception as e:
        return f"Error: {str(e)}"
def scientific_calc():
    try:
        expr = input("Enter expression :")
        result= eval(expr,{"__builtins__": None},{
            "sqrt": math.sqrt,
            "pow": math.pow,
            "factorial": math.factorial
        })
        history.append(f"{expr} = {result}")
        return result
    except Exception as e:
        return f"Error: {str(e)}"

#----Main Program----
print("....Welcome to command line calculator....!")
mode = "basic"
show_help()
while True:
    command = input(f"[{mode.capitalize()} Mode] >>>").strip().lower()
    if command == "quit":
        print("Goodbye!")
        break
    elif command == "help":
        show_help()
    elif command == "history":
        show_history()
    elif command == "save":
        save_history()
    elif command == "mode":
        mode = "Scientific" if mode =="basic" else "basic"
        print(f"Switched to {mode.capitalize()} Mode.")
    elif command =="":
        continue
    else:
        if mode == "basic":
            result = basic_calc()
        else:
            result = scientific_calc()
        print("Result:", result)
        
                

    
        

               
            
                   
