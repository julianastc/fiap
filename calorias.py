#quantos alimentos no dia e quantas calorias por alimento
#exibir calorias totais

food_amount = int(input("Quantos alimentos você consumiu hoje? "))

total_kcal = 0

for x in range(1, food_amount+1):
    food_kcal = int(input(f"Quantas calorias tem o alimento {x}? "))
    total_kcal = total_kcal + food_kcal
    
print(f"O total de calorias diária é {total_kcal}. ")