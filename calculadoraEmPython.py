def calcular():
    firstValue = input("Digite o primeiro valor: \n")
    operation = input("Digite a operação que vc quer fazer: +, -, *, / \n")
    secondValue = input("Digite o segundo valor: \n")  

    i = 0
    while operation != '+' and operation != '-' and operation != '*' and operation != '/':
        i += 1
        operation = input("Digite a operação que vc quer fazer: +, -, *, / \n")
        if i > 3:
            break


    def sum():
        adition = int(firstValue) + int(secondValue)
        print(f"O valor da operação é", adition)

    def substraction():
        substraction = int(firstValue) - int(secondValue)
        print(f"O valor da operação é", substraction)

    def multiply():
        multiply = int(firstValue) * int(secondValue)
        print(f"O valor da operação é", multiply)
    
    def divide():
        divide = int(firstValue) / int(secondValue)
        print(f"O valor da operação é", divide)


    if operation == '+':
        sum()

    elif operation == '-':
        substraction()

    elif operation == '*':
        multiply()

    elif operation == '/':
        divide()

    else:        
        print(f'Vc digitou {operation}, isso não é um sinal ou operação válida. Digite +, - ,* ou /')

calcular()