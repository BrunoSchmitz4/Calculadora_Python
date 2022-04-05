# Calculadora Python

#per_ini = 0

opcao = ""
valores = []
val1 = 0
val2 = 0

def soma ():
    print(f'A soma de {valores[0]} + {valores[0]} é: {valores[0] + valores[1]}')
def subtracao():

    print(f'A subtração de {valores[0]} - {valores[0]} é: {valores[0] - valores[1]}')

print("Bem vindo à calculadora Python! (Ou Cobrinha para mos mais íntimos da linguagem XD\n "
      "Escolha o tipo de cálculo que você deseja: \n- Adição (A)\n- Subtração (B)")

opcao = str(input("Opção: "))

if opcao == 'a' or opcao == 'A':
    val1 = float(input("Insira um valor inicial: "))
    valores.append(val1)
    val2 = float(input("Insira um outro valor: "))
    valores. append(val2)
    soma()
elif opcao == 'b' or opcao == 'B':
    val1 = float(input("Insira um valor inicial: "))
    valores.append(val1)
    val2 = float(input("Insira um outro valor: "))
    valores.append(val2)
    subtracao()