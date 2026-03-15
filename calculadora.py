import os

os.system ("cls")

print("Calculadora Simples")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("===========================================")
print("Escolha a operação: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Digite o número da operação: "))

if operacao ==1:
    resultado1 = num1 + num2
    print("===========================================")
    print(f"Resultado: {resultado1}")

elif operacao ==2:
    resultado2 = num1 - num2
    print("===========================================")
    print(f"Resultado: {resultado2}")

elif operacao ==3:
    resultado3 = num1 * num2
    print("===========================================")
    print(f"Resultado {resultado3}")

elif operacao ==4:
    resultado4 = num1 / num2
    print("===========================================")
    print(f"Resultado: {resultado4}")

else:
    print("===========================================")
    print("Operação inválida")