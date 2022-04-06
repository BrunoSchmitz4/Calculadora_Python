# Calculadora Python

menu_ini = 0

opcao = ""
valores = []
val1 = 0
val2 = 0

def soma ():
    print(f'A soma de {valores[0]} + {valores[1]} é: {valores[0] + valores[1]}')
def subtracao ():
    print(f'A subtração de {valores[0]} - {valores[1]} é: {valores[0] - valores[1]}')
def divisao ():
    print(f'A divisão de {valores[0]} % {valores[1]} é: {valores[0] / valores[1]}')
def multiplicacao ():
    print(f'A multiplicação de {valores[0]} * {valores[1]} é: {valores[0] * valores[1]}')

while menu_ini == 0:
    print("\n\nBem vindo à calculadora Python! (Ou Cobrinha para mos mais íntimos da linguagem XD\n "
      "Escolha o tipo de cálculo que você deseja: \n(A) - Adição\n(B) - Subtração\n(C) - Divisão\n(D)- Multiplicação \n(E) - Sair")
    opcao = str(input("Opção: "))

    if opcao == 'a' or opcao == 'A':
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0,val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1,val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        soma()
    elif opcao == 'b' or opcao == 'B':
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1, val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        subtracao()
    elif opcao == 'c' or opcao == 'C':
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1, val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        divisao()
    elif opcao == 'd' or opcao == 'D':
        val1 = float(input("Insira um valor inicial: "))
        valores.insert(0, val1)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        val2 = float(input("Insira um outro valor: "))
        valores.insert(1, val2)
        print(f'A quantidade de itens na lista atualmente é: {len(valores)}')
        multiplicacao()
    elif opcao == 'e' or opcao == 'E':
        print("Okay :3\nBye Bye! <3")
        menu_ini = 1