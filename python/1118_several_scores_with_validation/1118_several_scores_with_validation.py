media = 0
nota1 = 0
nota2 = 0


def pergunta():
    global media, nota1, nota2
    novo = int(input("novo calculo (1-sim 2-nao)\n"))
    if novo == 1:
        media = 0
        nota1 = 0
        nota2 = 0
        return False
    elif novo == 2:
        return True
    pergunta()

while True:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    elif nota1 == 0:
        nota1 += nota
    elif nota1 > 0:
        nota2 += nota
        media = (nota1+nota2)/2
        print(f"media = {media:.2f}")
        if pergunta():
            break
