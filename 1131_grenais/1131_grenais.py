inter = 0
gremeio = 0

while True:
    time, valor = map(int, input().split(" "))
    if time == 3:
        inter += 1
    elif time == 2:
        gremeio += 1
    novo = int(input("Novo grenal (1-sim 2-nao)\n"))
    if novo == 2:
        break
vencedor = "Inter" if inter > gremeio else "Gremio"
print(f"{inter+gremeio} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremeio}")
print("Empates:0")
print(f"{vencedor} venceu mais")