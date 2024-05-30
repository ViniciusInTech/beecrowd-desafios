inicio, fim = map(int, input().split(" "))

if inicio == 0 and fim == 0:
    print("O JOGO DUROU 24 HORA(S)")
elif inicio < fim:
    print(f"O JOGO DUROU {fim-inicio} HORA(S)")
else:
    duracao = (24 - inicio) + fim
    print(f"O JOGO DUROU {duracao} HORA(S)")