#  Projeto de Calculadora 

pergunta = input('Qual operação você deseja realizar? (+, -, *, /,): ')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if pergunta != '+' and pergunta != '-' and pergunta != '*' and pergunta != '/':
    print('Operação inválida. Por favor, escolha entre +, -, *, ou /.')
else:
    print(f'Você escolheu a operação: {pergunta}')

if pergunta == '+':
    resultado = num1 + num2
    print(f'O resultado da soma é: {resultado}')
elif pergunta == '-':
    resultado = num1 - num2
    print(f'O resultado da subtração é: {resultado}')
elif pergunta == '*':
    resultado = num1 * num2
    print(f'O resultado da multiplicação é: {resultado}')
elif pergunta == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f'O resultado da divisão é: {resultado}')
else:
        resultado = 'Erro: Divisão por zero não é permitida.'
        print(resultado)
    