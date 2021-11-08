#intergration project sprint 2
#Alaga Begic
#Prof. Vanselow

def main():
    print("Hello kids! Today we are going to practice math!")
    continue_program = True
    while continue_program:
        print("Please select a lesson to continue.")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit Course")
        kid_choice = int(input())
        if kid_choice == 1:
            addition_practice()
        elif kid_choice == 2:
            subtraction_practice()
        elif kid_choice == 3:
            multiplication_practice()
        elif kid_choice == 4:
            division_practice()
        elif kid_choice == 5:
            print("Great Job today!")
            print("Thank you for practicing with us and trying you best!")
            print("Hopefully you come again!")
            continue_program = False
        else:
            print("Please select a valid item from the lessons.")

def addition_practice():
    print("We are going to do some practice problems with addition.")
    addition_continue = True
    while addition_continue:
        prob_one = int(input("1. 5 + 5 = "))
        if prob_one != 10:
            prob_one = "1. Incorrect"
        else:
            prob_one = "1. Correct"
        prob_two = int(input("2. 27 + 27 = "))
        if prob_two == 54:
            prob_two = "2. Correct"
        else:
            prob_two = "2. Incorrect"
        prob_three = int(input("3. 163 + 234 = "))
        if prob_three < 397 or prob_three > 397:
            print("Close but something went wrong there.")
            prob_three = "3. Incorrect"
        else:
            print("Good job! That one was challenging one.")
            prob_three = "3. Correct"
        print("These are your results:")
        results_add = [prob_one, prob_two, prob_three]
        for x in results_add:
            print(x)
        print("That was some good practice.")
        print("If you would like to try again: ")
        print("Enter 1")
        print("If you would like to return to the main menu:")
        print("Enter 2")
        kid_decision = int(input())
        if kid_decision == 1:
            addition_continue = True
        elif kid_decision == 2:
            addition_continue = False
        else:
            addition_continue = False

def subtraction_practice():
    print("We are going to do some practice problems with subtraction.")
    subtraction_continue = True
    while subtraction_continue:
        prob_one = int(input("1. 7 - 5 = "))
        if subtraction_machine(7,5) == 2 and prob_one == 2:
            prob_one = "1. Correct"
        else:
            prob_one = "1. Incorrect"
        prob_two = int(input("1. 57 - 25 = "))
        if subtraction_machine(57,25) == prob_two:
            prob_two = "2. Correct"
        else:
            prob_two = "2. Incorrect"
        prob_three = int(input("3. 345 - 250 = "))
        if subtraction_machine(345,250) == prob_three:
            prob_three = "3. Correct"
        else:
            prob_three = "3. Incorrect"
        results = [prob_one, prob_two, prob_three]
        for x in results:
            print(x)
        print("That was some great work!")
        print("select 1 to try again or select 2 to go back to all lessons.")
        kid_decision = int(input())
        if kid_decision == 1:
            subtraction_continue = True
        else:
            subtraction_continue = False

def multiplication_practice():
    print("We are going to do some practice problems with multiplication!")
    print("These are going to be multiple choice.")
    multiplication_continue = True
    while multiplication_continue:
        prob_one = print("1. 2 * 7 = ")
        for x in range(1,5):
            if x == 1:
                print("A. 18",)
            elif x == 2:
                print("B. 14")
            elif x == 3:
                print("C. 12")
            else:
                print("D. 20")
        one_ans = input("Select answer: ")
        if one_ans == "B" or one_ans == "b":
            prob_one = "1. Correct"
        else:
            prob_one = "1. Incorrect"
        prob_two = print("2. 17 * 5 = ")
        for y in range(1,5):
            if y == 1:
                print("A. 85")
            elif y == 2:
                print("B. 80")
            elif y == 3:
                print("C. 97")
            else:
                print("D. 67")
        two_ans = input("Select answer: ")
        if two_ans == "A" or two_ans == "a":
            prob_two = "2. Correct"
        else:
            prob_two = "2. Incorrect"
        prob_three = print("3. 125 * 3 = ")
        for z in range(1,5):
            if z == 1:
                print("A. 400")
            elif z == 2:
                print("B. 350")
            elif z == 3:
                print("C. 425")
            else:
                print("D. 375")
        three_ans = input("Select Answer: ")
        if three_ans == "D" or three_ans == "d":
            prob_three = "3. Correct"
        else:
            prob_three = "3. Incorrect"
        results = [prob_one, prob_two, prob_three]
        for x in results:
            print(x)
        print("Great Job!")
        kid_decision = int(input("Select 1 to try again or 2 to return to all lessons: "))
        if kid_decision == 1:
            multiplication_continue = True
        else:
            multiplication_continue = False

def division_practice():
    print("We are going to do some practice problems with division!")
    division_continue = True
    while division_continue:
        prob_one = int(input("1. 16 / 4 = "))
        if prob_one == division_machine(16, 4):
            prob_one = "1. Correct"
        else:
            prob_one = "1. Incorrect"
        prob_two = int(input("2. 150 / 25 = "))
        if prob_two == division_machine(150, 25):
            prob_two = "2. Correct"
        else:
            prob_two = "2. Incorrect"
        prob_three = int(input("3. 1644 / 4 = "))
        if prob_three == division_machine(1644, 4):
            prob_three = "3. Correct"
        else:
            prob_three = "3. Incorrect"
        results = [prob_one, prob_two, prob_three]
        for x in results:
            print(x)
        print("Good Work!")
        kid_decision = int(input("Select 1 to try again or 2 to return to all lessons: "))
        if kid_decision == 1:
            division_continue = True
        else:
            division_continue = False

def division_machine(x, y):
    x /= y
    return x

def subtraction_machine(x, y):
    x -= y
    return x
main()

