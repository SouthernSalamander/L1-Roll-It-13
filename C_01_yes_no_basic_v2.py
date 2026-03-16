# functions go here

def yes_no(question):

    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check if user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Say yes / no")

# Main Routine

want_instructions = yes_no("Do you want to see the instructions? ")
want_coffee = yes_no("Do you want coffee? ")

if want_coffee == "yes":
    print("too bad lil bro I'm a computer\n")

if want_coffee == "no":
    print("good cause I don't got any\n")

print("we done")

