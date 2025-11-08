string = input()

if not string:  # Lista vazia
    print(0)
else:
    lista = []
    c = 1
    max_c = 1
    max_element = string[0]

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            c += 1
            if c > max_c:
                max_c = c
                max_element = string[i] # Atualiza o caractere com a maior repetição
        else:
            c = 1    # Se o caractere atual e o próximo forem diferentes, reseta o contador

    print(max_c)