_, dia_inicio = input().split(" ")
dia_inicio = int(dia_inicio)
horas_inicio, minutos_inicio, segundos_inicio = map(int, input().split(" : "))

_, dia_fim = input().split(" ")
dia_fim = int(dia_fim)
horas_fim, minutos_fim, segundos_fim = map(int, input().split(" : "))

dias = dia_fim - dia_inicio

inicio_em_segundos = horas_inicio * 3600 + minutos_inicio * 60 + segundos_inicio
fim_em_segundos = horas_fim * 3600 + minutos_fim * 60 + segundos_fim

if fim_em_segundos < inicio_em_segundos:
    fim_em_segundos += 24 * 3600
    dias -= 1

duracao_total = fim_em_segundos - inicio_em_segundos

duracao_horas = duracao_total // 3600
duracao_minutos = (duracao_total % 3600) // 60
duracao_segundos = duracao_total % 60

print(f"{dias} dia(s)")
print(f"{duracao_horas} hora(s)")
print(f"{duracao_minutos} minuto(s)")
print(f"{duracao_segundos} segundo(s)")
