tempo_de_viagem = int(input())
velocidade_media = int(input())

litros_necessarios = (tempo_de_viagem*velocidade_media)/12
print(f"{litros_necessarios:.3f}")