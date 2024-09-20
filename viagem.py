import math

valor_bruto = float(input("Qual o valor bruto da viagem? "))
categoria_assento = str(input("Qual a categoria do assento? ")).lower()
qntd_viajantes = int(input("Quantos passageiros serão? "))


if categoria_assento == "econômica" or "economica" and qntd_viajantes == 2:
    desconto = 3/100
elif categoria_assento == "econômica" or "economica" and qntd_viajantes == 3:
    desconto = 4/100
elif categoria_assento == "econômica" or "economica" and qntd_viajantes <=4:
    desconto = 5/100
    

if categoria_assento == "executiva" and qntd_viajantes == 2:
    desconto = 5/100
elif categoria_assento == "executiva" and qntd_viajantes == 3:
    desconto = 7/100
elif categoria_assento == "executiva" and qntd_viajantes <=4:
    desconto = 8/100
    

if categoria_assento == "primeira classe" and qntd_viajantes == 2:
    desconto = 10/100
elif categoria_assento == "primeira classe" and qntd_viajantes == 3:
    desconto = 15/100
elif categoria_assento == "primeira classe" and qntd_viajantes <=4:
    desconto = 20/100
    
valor_desc = desconto * valor_bruto
valor_liq = valor_bruto - valor_desc
valor_medio = valor_liq / qntd_viajantes

print(f"""
      
      Valor bruto: {valor_bruto:.2f}
      Valor do desconto: {valor_desc:.2f}
      Valor líquido: {valor_liq:.2f}
      Valor médio por passageiro: {valor_medio:.2f}
      """)