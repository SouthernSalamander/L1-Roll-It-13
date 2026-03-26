
# initialise list to hold game history
game_history = []

# get data (base component does this already, code below for testing purposes)

while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break

    user_points = int(input("User points? "))
    cpu_points = int(input("CPU points? "))
    winner = input("Who won? ")
    user_score = int(input("User score: "))
    cpu_score = int(input("CPU score: "))

    game_results = (f"Round {rounds_played}: User Points: {user_points} | "
                    f"CPU Score: {cpu_points}, {winner} wins ({user_score} | {cpu_score})")

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)
