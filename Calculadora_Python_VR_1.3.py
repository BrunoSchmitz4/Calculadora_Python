import math
# Calculadora Python

menu_ini = 0

pi = 3.14159265
opcao = ""
valores = []
val1 = 0
val2 = 0

def soma ():
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'A soma de {valores[0]} + {valores[1]} é: {valores[0] + valores[1]}')

def subtracao ():
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'A subtração de {valores[0]} - {valores[1]} é: {valores[0] - valores[1]}')

def divisao ():
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'A divisão de {valores[0]} % {valores[1]} é: {valores[0] / valores[1]}')

def multiplicacao ():
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'A multiplicação de {valores[0]} x {valores[1]} é: {valores[0] * valores[1]}')

def resto ():
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'O resto de {valores[0]} % {valores[1]} é: {valores[0] % valores[1]}')

def r_quadrada ():
    valores.clear()
    print("Que tipo de operação deseja efetuar com a raiz quadrada?"
          "\n(A) - Adição\n(B) - Subtração\n(C) - Divisão\n(D) - Multiplicação\n(E) - Resto de divisão\n(F) - Valor de uma raiz")
    opcao = str(input("Opção: "))
    if opcao == 'a' or opcao == 'A':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1, val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        print(f'A soma da raiz quadrada de {valores[0]} + {valores[1]} é: {math.sqrt(valores[0]) + math.sqrt(valores[1])}')
    elif opcao == 'b' or opcao == 'B':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1, val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        print(
            f'A subtração da raiz quadrada de {valores[0]} - {valores[1]} é: {math.sqrt(valores[0]) - math.sqrt(valores[1])}')
    elif opcao == 'c' or opcao == 'C':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1, val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        print(f'A divisão da raiz quadrada de {valores[0]} % {valores[1]} é: {math.sqrt(valores[0]) / math.sqrt(valores[1])}')
    elif opcao == 'd' or opcao == 'D':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1, val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        print(f'A soma da raiz quadrada de {valores[0]} x {valores[1]} é: {math.sqrt(valores[0]) * math.sqrt(valores[1])}')
    elif opcao == 'e' or opcao == 'E':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1, val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        print(
            f'O resto da divisão da raiz quadrada de {valores[0]} % {valores[1]} é: {math.sqrt(valores[0]) % math.sqrt(valores[1])}')
    elif opcao == 'f' or opcao == 'F':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A raiz quadrada de {valores[0]} é {math.sqrt(valores[0])}')

while menu_ini == 0:
    print("\n\nBem vindo à calculadora Python! (Ou Cobrinha para os mais íntimos da linguagem XD)\n "
      "Escolha o tipo de cálculo que você deseja: \n(A) - Adição\n(B) - Subtração\n(C) - Divisão\n(D) - Multiplicação\n(E) - Resto de divisão\n(F) - Raiz Quadrada \n(Z) - Sair")
    opcao = str(input("Opção: "))

    if opcao == 'a' or opcao == 'A':
        soma()
    elif opcao == 'b' or opcao == 'B':
        subtracao()
    elif opcao == 'c' or opcao == 'C':
        divisao()
    elif opcao == 'd' or opcao == 'D':
        multiplicacao()
    elif opcao == 'e' or opcao == 'E':
        resto()
    elif opcao == 'f' or opcao == 'F':
        r_quadrada()
    elif opcao == 'z' or opcao == 'Z':
        print("Okay :3\nBye Bye! <3")
        menu_ini = 1
    else:
        menu_ini = 1
        if menu_ini == 1:
            print("\n\nOpa! Está não é uma opção! *-*\nTente novamente:")
            menu_ini = 0