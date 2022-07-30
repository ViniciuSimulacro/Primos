num = 0
numero = int(input('Digite um numero para saber se é primo: '))
def primos(num):
    divisor = 1
    cont = 1
   
    while cont < numero+1:
        resultado = 0
        resultado = numero % divisor
        if resultado == 0:
            cont += 1
        
        if numero == 1 or cont > 2:
            print(f'O numero {numero} não é primo')
            break
                
        if numero == divisor+1 and cont == 2:
            print(f'O numero {numero} é primo ')
            break

        divisor += 1


for n in range(1,numero+1):
    numero = n
    primos(n)
