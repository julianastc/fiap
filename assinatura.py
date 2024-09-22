type_plan = int(input("""Qual o tipo do plano? 
                  1 - Basic
                  2 - Silver 
                  3 - Gold
                  4 - Platinum 
                  """))
basic_plan = 1 
silver_plan = 2 
gold_plan = 3 
platinum_plan = 4 

yearly_income = float(input("Qual foi o faturamento anual? "))
bonus = 0

if type_plan == 1:
    bonus = yearly_income * 30/100
if type_plan == 2:
    bonus = yearly_income * 20/100
if type_plan == 3:
    bonus = yearly_income * 10/100
if type_plan == 4:
    bonus = yearly_income * 5/100
    
print(f"O valor do bonus é {bonus:.2f}")