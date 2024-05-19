def truthtable():
    var = []
    NoVariable = 0
    print("=>this code handle variables max of 4!\n=>variables should from ABCD sequentially!\n=>provide the number of the variables appeared in the expression\n=>insert expression.\n=>Enter 'help' for help\n=>______________________________________________________________________________")
    expression = (input("enter your expression: "))
    Variables = expression.split(" ")
    for i in Variables:
        if len(i) == 1:
            NoVariable+=1
            var.append(i)
    if (expression != "help"):
        print("\033[92mRESUlT\033[0m")
    
    x = NoVariable
    if x == 1:
        print("A", " | ", "negation")
        print("-------")
    elif x == 2:
        print("A", "|", "B", "| ", expression)
        print("----------")
    elif x == 3:
        print("A", "|", "B", "|", "C", "| ", expression)
        print("----------")
    else:
        print("A", "|", "B", "|", "C", "|", "D", "| ", expression)
        print("----------")

    min_term = []  # List to store the minimum terms
    max_term = []  # List to store the maximum terms

    for A in range(2):
        if x == 1:
            result = int(eval(expression))
            print(A, " | ", result)
            if result == 1:
                min_term.append(f"{'A' if A==1 else 'A̅'}")
            else:
                max_term.append(f"{'A' if A == 0 else 'A̅'}")
        else:
            for B in range(2):
                if x == 2:
                    result = int(eval(expression))
                    print(A, "|", B, "|", result)
                    if result == 1:
                        min_term.append(f"{'A' if A == 1 else 'A̅'} {'B' if B == 1 else 'B̅'}")
                    else:
                        max_term.append(f"{'A' if A == 0 else 'A̅'}+{'B' if B == 0 else 'B̅'}")
                else:
                    for C in range(2):
                        if x == 3:
                            result = int(eval(expression))
                            print(A, "|", B, "|", C, "|", result)
                            if result == 1:
                                min_term.append(f"{'A' if A == 1 else 'A̅'}{'B' if B == 1 else 'B̅'}{'C' if C == 1 else 'C̅'}")
                            else:
                                max_term.append(f"{'A' if A == 0 else 'A'}+{'B' if B == 0 else 'B̅'}+{'C' if C == 0 else 'C̅'}")
                        else:
                            for D in range(2):
                                result = int(eval(expression))
                                print(A, "|", B, "|", C, "|", D, "|", result)
                                if result == 1:
                                    min_term.append(f"{'A' if A == 1 else 'A̅'}{'B' if B == 1 else 'B̅'}{'C' if C == 1 else 'C̅'}{'D' if D == 1 else 'D̅'}")
                                else:
                                    max_term.append(f"{'A' if A == 0 else 'A̅'}+{'B' if B == 0 else 'B̅'}+{'C' if C == 0 else 'C̅'}+{'D' if D == 0 else 'D̅'}")

    print("\nMinimum Term: ", " + ".join(min_term))
    #print(min_term)
    print("Maximum Term: ", " * ".join(max_term))

truthtable()
