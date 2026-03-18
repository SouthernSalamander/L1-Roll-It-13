import random

# Initialize rounds points
user_points = 0
cpu_points = 0
double_user = "no"

# Roll the dice for the user and note if they got a double
user_one = random.randint(1, 6)
user_two = random.randint(1, 6)

if user_one == user_two:
    double_user = "yes"


# Roll the dice for the computer
cpu_one = random.randint(1, 6)
cpu_two = random.randint(1, 6)

# Update the user / computer points
user_points += user_one + user_two
cpu_points += cpu_one + cpu_two

# Output the results
print("\nInitial Points")
print(f"User    - Roll 1: {user_one} \t| Roll 2: {user_two} \t| Total: {user_points}")
print(f"CPU     - Roll 1: {cpu_one} \t| Roll 2: {cpu_two} \t| Total: {cpu_points}")

# Let the user know if the qualify for double points
if double_user == "yes":
    print("\nYou got a double!")
    print("If you win this round, you'll get double points")