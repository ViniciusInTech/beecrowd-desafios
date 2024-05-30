pergunta_a = input()
pergunta_b = input()
pergunta_c = input()

def vertebrado(pergunta_b, pergunta_c):
    especie = "ave" if pergunta_b == "ave" else "mamifero"
    if especie == "ave":
        return "aguia" if pergunta_c == "carnivoro" else "pomba"
    return "homem" if pergunta_c == "onivoro" else "vaca"


def invertebrado(pergunta_b, pergunta_c):
    especie = "inseto" if pergunta_b == "inseto" else "anelideo"
    if especie == "inseto":
        return "pulga" if pergunta_c == "hematofago" else "lagarta"
    return "sanguessuga" if pergunta_c == "hematofago" else "minhoca"

animal = vertebrado(pergunta_b, pergunta_c) if pergunta_a == "vertebrado" else invertebrado(pergunta_b, pergunta_c)

print(animal)