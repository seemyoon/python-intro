# 1. Create a loop in which you need to ask the user to enter two numbers in the terminal
# 2. Print the result of the division of the first number by the second number in the terminal
# 3. After that, ask the user if he wants to continue yes/no
# 4. If the answer is no, you need to exit the loop
# 5. Otherwise, you need to repeat everything again

while True:
    try:
        user_first_number = int(input("enter the number to be divided: "))
        user_second_number = int(input("enter the divisor: "))

        if user_second_number == 0:
            print("division by zero is not allowed!")
            continue

        result = user_first_number / user_second_number
        print(f"result of division: {result}")

        while True:
            user_answer_input = input("do you want to continue? ").strip().lower()
            if user_answer_input == "yes":
                break
            elif user_answer_input == "no":
                exit()
            else:
                print("you need set 'yes' or 'no'")

    except ValueError as e:
        print(e)
        print("you entered wrong type of value")
