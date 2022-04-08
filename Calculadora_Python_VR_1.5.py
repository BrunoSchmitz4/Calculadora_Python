import math

# Calculadora Python

menu_ini = 0
pi = 3.14159265
opcao = ""
valores = []
val1 = 0
val2 = 0

def soma (): # Função para cálculos de soma
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'A soma de {valores[0]} + {valores[1]} é: {valores[0] + valores[1]}')

def subtracao (): # Função para cálculos de subtração
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'A subtração de {valores[0]} - {valores[1]} é: {valores[0] - valores[1]}')

def divisao (): # Função para cálculos de divisão
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'A divisão de {valores[0]} % {valores[1]} é: {valores[0] / valores[1]}')

def multiplicacao (): # Função para cálculos de multiplicação
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'A multiplicação de {valores[0]} x {valores[1]} é: {valores[0] * valores[1]}')

def resto (): # Função para restos de divisão
    valores.clear()
    val1 = float(input("Insira um valor inicial: "))
    valores.insert(0, val1)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    val2 = float(input("Insira um outro valor: "))
    valores.insert(1, val2)
    print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
    print(f'O resto de {valores[0]} % {valores[1]} é: {valores[0] % valores[1]}')

def r_quadrada (): # Função para cálculos envolvendo a raiz quadrada
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

def tabuada (): # Função para gerar tabuadas personalizadas
    valores.clear()
    val1 = int(input("Insira um número: "))
    valores.insert(0, val1)
    val2 = int(input("Digite até que número a tabuada deve prosseguir: "))
    valores.insert(1, val2)
    tab = 0
    while tab <= val2:
        print(f'{tab} X {val1}: {tab * val1}')
        tab += 1

def qc_pot () : # Função para cálculos envolvendo a exponenciação
    valores.clear()
    print("Que tipo de operação deseja efetuar com exponenciação?"
          "\n(A) - Adição\n(B) - Subtração\n(C) - Divisão\n(D) - Multiplicação\n(E) - Resto de divisão\n(F) - Valor de uma exponenciação")
    opcao = str(input("Opção: "))
    if opcao == 'a' or opcao == 'A':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val2)
        val3 = float(input("Insira um segundo valor: "))
        valores.insert(0, val3)
        val4 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val4)
        print(f'A soma de {val1} em sua {val2}° potência + {val3} em sua {val4}° é: {math.pow(val1, val2) + math.pow(val3, val4)}')
    elif opcao == 'b' or opcao == 'B':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val2)
        val3 = float(input("Insira um segundo valor: "))
        valores.insert(0, val3)
        val4 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val4)
        print(f'A subtração de {val1} em sua {val2}° potência - {val3} em sua {val4}° é: {math.pow(val1, val2) - math.pow(val3, val4)}')
    elif opcao == 'c' or opcao == 'C':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val2)
        val3 = float(input("Insira um segundo valor: "))
        valores.insert(0, val3)
        val4 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val4)
        print(f'A divisão de {val1} em sua {val2}° potência % {val3} em sua {val4}° é: {math.pow(val1, val2) / math.pow(val3, val4)}')
    elif opcao == 'd' or opcao == 'D':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val2)
        val3 = float(input("Insira um segundo valor: "))
        valores.insert(0, val3)
        val4 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val4)
        print(f'A multiplicação de {val1} em sua {val2}° potência % {val3} em sua {val4}° é: {math.pow(val1, val2) * math.pow(val3, val4)}')
    elif opcao == 'e' or opcao == 'E':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val2)
        val3 = float(input("Insira um segundo valor: "))
        valores.insert(0, val3)
        val4 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val4)
        print(f'O resto de divisão {val1} em sua {val2}° potência % {val3} em sua {val4}° é: {math.pow(val1, val2) % math.pow(val3, val4)}')
    elif opcao == 'f' or opcao == 'F':
        valores.clear()
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = float(input("Insira o valor da potência desejada: "))
        valores.insert(1, val2)
        print(f'O valor de {val1} em sua {val2}° potência é: {math.pow(val1, val2)}')

def factor (): # Função para cálculos envolvendo números fatoriais
    valores.clear()
    print("Que tipo de operação deseja efetuar com fatoriais?"
          "\n(A) - Adição\n(B) - Subtração\n(C) - Divisão\n(D) - Multiplicação\n(E) - Resto de divisão\n(F) - Valor de um número fatorial")
    opcao = str(input("Opção: "))
    if opcao == 'a' or opcao == 'A':
        valores.clear()
        val1 = int(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = int(input("Insira um segundo valor: "))
        valores.insert(1, val2)
        print(f'A soma de {val1}! + {val2}! é: {math.factorial(val1) + math.factorial(val2)}')
    elif opcao == 'b' or opcao == 'B':
        valores.clear()
        val1 = int(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = int(input("Insira um segundo valor: "))
        valores.insert(1, val2)
        print(f'A subtração de {val1}! - {val2}! é: {math.factorial(val1) - math.factorial(val2)}')
    elif opcao == 'c' or opcao == 'C':
        valores.clear()
        val1 = int(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = int(input("Insira um segundo valor: "))
        valores.insert(1, val2)
        print(f'A divisão de {val1}! % {val2}! é: {math.factorial(val1) / math.factorial(val2)}')
    elif opcao == 'd' or opcao == 'D':
        valores.clear()
        val1 = int(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = int(input("Insira um segundo valor: "))
        valores.insert(1, val2)
        print(f'A multiplicação de {val1}! X {val2}! é: {math.factorial(val1) * math.factorial(val2)}')
    elif opcao == 'e' or opcao == 'E':
        valores.clear()
        val1 = int(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        val2 = int(input("Insira um segundo valor: "))
        valores.insert(1, val2)
        print(f'O resto da divisão de {val1}! % {val2}! é: {math.factorial(val1) % math.factorial(val2)}')
    elif opcao == 'f' or opcao == 'F':
        valores.clear()
        val1 = int(input("Insira um valor: "))
        valores.insert(0, val1)
        print(f'O valor fatorial de {val1}! é: {math.factorial(val1)}')


while menu_ini == 0:
    print("\n\nBem vindo à calculadora Python! (Ou Cobrinha para os mais íntimos da linguagem XD)\n "
      "Escolha o tipo de cálculo que você deseja: \n(A) - Adição\n(B) - Subtração\n(C) - Divisão\n(D) - Multiplicação"
          "\n(E) - Resto de divisão\n(F) - Raiz Quadrada\n(G) - Criar tabuada\n(H) - Exponenciação\n(I) - Fatorial\n(Z) - Sair")
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
    elif opcao == 'g' or opcao == 'G':
        tabuada()
    elif opcao == 'h' or opcao == 'H':
        qc_pot()
    elif opcao == 'i' or opcao == 'I':
        factor()
    elif opcao == 'z' or opcao == 'Z':
        print("Okay :3\nBye Bye! <3")
        menu_ini = 1
    else:
        menu_ini = 1
        if menu_ini == 1:
            print("\n\nOpa! Está não é uma opção! *-*\nTente novamente:")
            menu_ini = 0