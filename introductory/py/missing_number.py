n = int(input())
numbers = set(map(int, input().split()))

for i in range(1, n + 1):   # Verifica cada número de 1 a n + 1
    if i not in numbers:    # Se esse número não estiver no conjunto, é o número faltante
        print(i)
        break