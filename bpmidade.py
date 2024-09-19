bpm = int(input("Indique seu BPM "))
idade = int(input("Qual sua idade? "))

bebe = 0 <= idade <= 2 
crianca = 8 <= idade <= 17
adulto = 18 <= idade <= 59
idoso = 60 <= idade 

bpm_bebe = 120 <= bpm <= 140
bpm_crianca = 80 <= bpm <= 100
bpm_adulto = 70 <= bpm <= 80
bpm_idoso = 50 <= bpm <= 60

if bebe and bpm == bpm_bebe:
    print("O bpm está dentro da faixa adequada")
elif bebe and bpm > 140:
    print("o bpm está acima da faixa adequada ")
elif bebe and bpm < 120:
    print("o bpm está abaixo da faixa adequada")

if crianca and bpm == bpm_crianca:
    print("O bpm está dentro da faixa adequada")
elif crianca and bpm > 100:
    print("O bpm está acima da faixa adequada")
elif crianca and bpm < 80:
    print("O bpm está abaixo da faixa adequada")
    
if adulto and bpm == bpm_adulto:
    print("O bpm está dentro da faixa adequada")
elif adulto and bpm > 80:
    print("O bpm está acima da faixa adequada")
elif adulto and bpm_adulto < 70:
    print("O bpm está abaixo da faixa adequada")
    
if idoso and bpm == bpm_idoso:
    print("O bpm está dentro da faixa adequada")
elif idoso and bpm > 60:
    print("O bpm está acima da faixa adequada")
elif idoso and bpm < 50:
    print("O bpm está abaixo da faixa adequada")