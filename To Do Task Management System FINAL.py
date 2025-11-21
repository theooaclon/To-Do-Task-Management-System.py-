repeat = True
confirm = "yes"
confirm2 = "no"
yes = "yes"
no = "no"
tasks = []         # LIST ALL TASK


# Start loop
while repeat == True:
    password = ""
    username = ""
    while username != "user":
        username = input("Please enter username: ")
        if username != "user":
            print("Incorrect username, try again!")
    while password != "defended":
        password = input("Enter Password: ")
        if password != "defended":
            print("Incorrect password, try again!")
    print("Access Granted!")


# MAIN MENU LOOP
    while repeat == True:
        print("======= MAIN MENU ======= \n1. Add Task \n2. View task \n3. Delete task \n4. Logout \n5. Exit")
        while repeat == True:
            try:
                user_choice = int(input("Hello, " + username + "! Please choose a number from the main menu: " ))
                break
            except ValueError:             # PRINT IF THE USER INPUT WORDS INSTEAD OF NUMBERS
                print("Invalid input, please enter a NUMBER")
                
        if user_choice==1:
            task = input("Enter task name: ")
            deadlines = input("Add deadline and date: ")
            tasks.append({"task": task, "deadlines": deadlines})      # THIS FUNCTION ADDS IT INTO THE LIST 
            print("=== TASK ADDED SUCCESSFULLY! ===")

        elif user_choice==2:
            if not tasks:
                print("=== NO TASKS ADDED! ===")                  # CHECK IF THERE'S A TASK LIST ADDED
            
            else:
                print("=== ALL TASKS LIST ===")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task["task"]} - {task["deadlines"]}")

        elif user_choice==3:
            if not tasks:
                print("=== NO TASKS ADDED TO DELETE! ===")
            

            else:
                print("=== ALL TASKS LIST! ===")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task['task']} - {task['deadlines']}")

                try:
                    while repeat==True:
                        delete = int(input("Please enter a number to delete: "))

                        if 1 <= delete <= len(tasks):
                            confirm = input("Are you sure you want to delete this (Yes/No): ").lower()    # VERIFYING IF THE USER WANTS TO DELETE OR NO
                            if confirm == yes:
                                removed = tasks.pop(delete - 1)
                                print(f"{delete}. {removed['task']} - {removed['deadlines']}, deleted sucessfully!")
                                break

                            elif confirm2 == no:
                                print("Deletion Canceled!")
                                break
                        else:
                            print("Invalid choices, try again!")
                                
                except ValueError:
                    print("Invalid choices, please enter a NUMBER")


        elif user_choice==4:
            print("Logout.. Returning to start!")
            break
    
        elif user_choice==5:
            print("Thank you for your time!")        # END OF THE SYSTEM
            exit()
         
        else:
            print("Invalid input, try again!")
