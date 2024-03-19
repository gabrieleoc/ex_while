"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
"""
import os
s = 'fm'
ec = 'scvds'
while True:
    nome = input('Digite seu nome: ')
    if len(nome) >= 3:
        print('-'* 25)
    else:
        print("nome inválido.")
        os.system("cls")
        continue
    
    idade = int(input('Digite sua idade: '))
    if idade in range(0,150):
        print('-'* 25)
    else:
        print('idade inválida.')
        os.system("cls")
        continue
        
    salario = int(input('Qual o seu salário? '))
    if salario > 0:
        print('-'* 25)
    else:
        print("salário inválido.")
        os.system("cls")
        continue
    
    sexo = input('f ou m: ')
    if sexo in s:
        print('-'* 25)
    else:
        print("sexo inválido.")
        os.system("cls")
        continue
    
    estado_civil = input("'s', 'c', 'v', 'd': ")
    if estado_civil in ec:
       
        print('-'* 25)
        print("Todas as entradas são válidas.")
        break
    else:
        print("estado civil inválido.")
        os.system("cls")
        continue
   
    
    

  