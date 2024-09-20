
total_transactions = int(input("Quantas transacoes você fez hoje? "))

total_spent = 0

for x in range(1, total_transactions+1):
    current_transaction = int(input(f"Qual o valor da transacao {x}? R$"))
    total_spent = total_spent + current_transaction
    
print(f"""Valor total gasto: R${total_spent:.2f}. 
 Média do valor de cada transacao: {total_spent / total_transactions:.2f} """)