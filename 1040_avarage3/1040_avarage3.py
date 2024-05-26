n1, n2, n3, n4 = map(float, input().split())

n1_peso = 2
n2_peso = 3
n3_peso = 4
n4_peso = 1

media = ((n1 * n1_peso) + (n2 * n2_peso) + (n3 * n3_peso) + (n4 * n4_peso)) / (n1_peso + n2_peso + n3_peso + n4_peso)

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")

    media_final = (media + nota_exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {media_final:.1f}")
