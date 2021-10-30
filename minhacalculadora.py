# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:52:32 2021

@author: marce
"""

# mostrar mensagem na tela
print("Selecione o número da operação desejada:")
print("")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("")

op = int(input("Digite sua opção (1/2/3/4):"))

#condição para saber se opção anterior existe
# mostrar próximo passo de determinar os números que vão participar da operação 
if op > 4 :
    print("Essa opção não é válida!")
else:
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    
#pegar os valores oferecidos e calcular a operação indicada
if op == 1:
    result = n1 + n2
    print("O resultado é: %r" %(result))
elif op == 2:
    result1 = n1 - n2
    print("O resultado é: %s" %(result1))
elif op == 3:
    result2 = n1 * n2
    print("O resultado é: %r" %(result2))
else:
    result3 = n1/n2
    print("O resultado é: %s" %(result3))