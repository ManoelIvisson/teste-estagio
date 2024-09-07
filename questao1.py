a = 0
b = 1
c = 0

# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)

entrada = int(input("Digite um número qualquer: "))

while a < entrada:
#   print(a) 
    c = a + b
    a = b
    b = c 

if a == entrada:
    print(f'{entrada} está na sequência de Fiboanacci')
else:
    print(f'{entrada} não está na sequência de Fibonacci')