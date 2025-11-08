n = int(input())

if n == 1:
    print("1")
elif n <= 3:
    print("NO SOLUTION")
else:
    pares = [str(i) for i in range(2, n + 1, 2)]  # Todos os pares
    impares = [str(i) for i in range(1, n + 1, 2)]  # Todos os ímpares

    resultado = pares + impares
    print(' '.join(resultado))