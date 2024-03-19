"""Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido.
"""
while True:
    entrada = input('Digite uma nota entre 0 e 10: ')
    entrada_int = int(entrada)
    
    if entrada_int in range(0,10):
        print(f'Valor {entrada} é válido.')
        break
    elif entrada_int > 10:
        print(f'Valor {entrada} é inválido.')
        continue
    else:
        print('isso nao pode aparecer')
    
    