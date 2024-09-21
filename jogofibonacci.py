# 1 1 2 3 5 8 13 21 34 55

input_answer = 0
current_fibonacci = 1
previous_fibonacci = 0

input_answer = int(input("Digite um valor inteiro "))

while (input_answer > current_fibonacci):
    refresh_fibonacci = current_fibonacci
    current_fibonacci = current_fibonacci + previous_fibonacci
    previous_fibonacci = refresh_fibonacci
   
if input_answer == current_fibonacci:
    print("Acao bem-sucedida!")   
else: 
    print("Acao falhou...")
