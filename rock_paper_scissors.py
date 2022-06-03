import random 
win_counter = 0
lose_counter = 0

while True:
	options = ["Rock", "Paper", "Scissors"]
	computer_choice = random.choice(options)
	player_choice = input("Make your choice: ")
	if player_choice.lower() == computer_choice.lower():
		print(f"You Won!")
		win_counter += 1
	elif player_choice.lower() == "stop":
		if win_counter > 0:
			print(f"You Won {win_counter} times")
		break
	else:
		print(f"You Lost")
		lose_counter += 1