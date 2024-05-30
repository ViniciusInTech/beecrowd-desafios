hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split(" "))

inicio_em_minutos = hora_inicio * 60 + minuto_inicio
fim_em_minutos = hora_fim * 60 + minuto_fim

if fim_em_minutos <= inicio_em_minutos:
    fim_em_minutos += 24 * 60

duracao_total = fim_em_minutos - inicio_em_minutos

duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
