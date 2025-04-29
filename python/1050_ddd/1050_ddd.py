ddd = int(input())

ddd_dic = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

estado = ddd_dic[ddd] if ddd in ddd_dic else "DDD nao cadastrado"
print(estado)