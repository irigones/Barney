print("Digite um número:")
a=float(input())
print('''Qual operação você quer fazer?
1/x = Inverso
* = Multiplicação
+ = Adição
/ = Divisão
- = Subtração
x² = elevado''')                # se colocar 3 aspas simples, consecutivas, pode continuar o mesmo código na linha só que na linha de baixo.
c=input()

if c=="1/x":
    print(1/a)
    quit()                      # "quit()" significa depois da ação de cima ele vai finalizar o programa. 

print("Digite algum outro número:")
b=float(input())



if c=="*":                      # "if" é para fazer uma condição, se for algum simbolo especifico, vai acontecer alguma coisa em especifico.
    print(a*b)

elif c=="+":                    # elif = else + if.
    print(a+b)

elif c=="/":                    # para fazer a condição funcionar, sempre botar ":" no final do código.
    print(a/b)

elif c=="-":                    # quando usar uma condição, como o "elif", na linha de baixo botar a condição com um tab antes.
    print(a-b)

elif c=="x²":
    print(a**b)                 # 1 "*" significa multiplicação, mas quando são 2 "*", significa elevado a algum número.
    