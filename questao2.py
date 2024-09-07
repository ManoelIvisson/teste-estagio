palavra = input('Digite uma palavra qualquer: ')

palavra = palavra.lower()

if 'a' in palavra:
    quantidade_a = 0

    for letra in palavra:
        if 'a' == letra:
            quantidade_a += 1
    
    print(f"Existem {quantidade_a} a's na String")

else:
    print('Letra "a" não se encontra na String')