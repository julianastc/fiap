# password = "LIBERDADE" + fatorial

current_minutes = int(input("Qual o minuto atual? "))
total_fatorial = 0
result_previous_fatorial = 1

for x in range (2, current_minutes + 1):
    result_current_fatorial = x * result_previous_fatorial
    result_previous_fatorial = result_current_fatorial
    total_fatorial = result_previous_fatorial

print(f"A senha é LIBERDADE{total_fatorial} ")