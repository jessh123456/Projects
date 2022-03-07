def integer_checker(question1):
    valid = False
    while not valid:
        error = "Whoops!, you must enter a positive number of a school age" \
                " kid!"
        try:
            response = int(input(question1))
            if 0 < response <= 120:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


choice = 0
students = ["Gilbert", "Bob", "Ana"]
name = ""
remove_name = ""
repeat = 1
num_children = 0
num_hours = 0
total_charge = 0
while choice != 5:
    print(
        "-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print(
        "-----------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()
    if choice == 1:
        name = input("What is the name of your child you would like to check "
                     "in?\n:").title()
        students.append(name)
    elif choice == 2:
        while repeat == 1:
            remove_name = input(
                "What is the name of your child that you would "
                "like to check out? \n:")
            if remove_name not in students:
                print("Sorry, this child does not seem to exist in our records"
                      " please try again.").title()
            elif remove_name in students:
                removed_student = students.index(remove_name)
                students.pop(removed_student)
                repeat = 0
                print(f"Thankyou! {remove_name} has been checked out!")
    elif choice == 3:
        print("---------------------------------")
        print("     **Calculating charge**")
        print("---------------------------------")
        num_children = integer_checker("How many children were checked in?\n:")
        num_hours = integer_checker("How many hour(s) was your kid(s) looked "
                                    "after for?\n:")
        total_charge = num_hours * 12 * num_children
        print(f"The total charge has come to ${total_charge}")
    elif choice == 4:
        print("Below is the list of Children who have been checked into the "
              "MGS Childcare program:")
        print(students)
    else:
        print("Goodbye")
        quit()
