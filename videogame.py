print("""Bem-vindo a votacao para escolher um videogame. 
      Para votar em XBOX digite 1
      Para votar em Playstation digite 2
      Para votar em Nintendo digite 3
      
      """)

xbox = 0
playstation = 0
nintendo = 0

vote_one = int(input("Qual o voto da primeira pessoa?"))
vote_two = int(input("Qual o voto da segunda pessoa? "))
vote_three = int(input("Qual o voto da terceira pessoa? "))
vote_four = int(input("Qual o voto da quarta pessoa? "))
vote_five = int(input("Qual o voto da quinta pessoa? "))

#votes
if vote_one == 1:
    xbox += 1
elif vote_one == 2:
   playstation += 1
elif vote_one == 3:
    nintendo += 1
else:
    print("Voto inválido.")
    
if vote_two == 1:
    xbox += 1
elif vote_two == 2:
    playstation += 1
elif vote_two == 3:
    nintendo += 1
else:
    print("Voto inválido.")
    
if vote_three == 1:
    xbox += 1
elif vote_three == 2:
    playstation += 1
elif vote_three == 3:
    nintendo += 1
else:
    print("Voto inválido.")
    
if vote_four == 1:
    xbox += 1
elif vote_four == 2:
    playstation += 1
elif vote_four == 3:
    nintendo += 1
else:
    print("Voto inválido.")
    
if vote_five == 1:
    xbox += 1
elif vote_five == 2:
    playstation += 1
elif vote_five == 3:
    nintendo += 1
else:
    print("Voto inválido.")

#results

if xbox > playstation and xbox > nintendo:
    print(f"Xbox foi o escolhido com {xbox} votos!")
elif playstation > xbox and playstation > nintendo:
    print(f"Playstation foi o escolhido com {playstation} votos!")
elif nintendo > xbox and nintendo > playstation:
    print(f"Nintendo foi o escolhido com {nintendo} votos!")
else:
    print("Houve empate!")