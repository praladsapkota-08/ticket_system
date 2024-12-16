import database
import datetime as time

while True:
    print("---------------WELCOME TO PARKING SYSTEM------------------")
    print("---------------CHOOSE OPTION------------------------------")
    print("----------------1 - CREATE TABLE--------------------------")
    print("----------------2 - VECHILE ENTRY-------------------------")

    try:

        choice = int(input("Give your choice 1 or 2"))

        if choice == 1:
            if database.checking_table():
                print("Table already exist")


            else:
                database.create_table()
                print('Table is created')

        if choice == 2:
            username = input("Enter your name: ")
            phone = input('Enter your phone number: ')
            vehicle_number = input('Enter your vehicle number: ')
            entry_time = time.datetime.now()

            try:

                vehicle = int(input("Enter 1 for two wheeler and 2 for four wheeler: "))
                print(vehicle, type(vehicle))
                print(vehicle in [1 , 2])
        
                if vehicle not in [1 , 2]:
                    print("Invalid details\nPlease enter number 1 or 2")
                    vehicle = int(input("Enter 1 for two wheeler and 2 for four wheeler: "))

                
                database.inserting_value(username,phone,vehicle_number,entry_time,vehicle)
                database.create_slip()

            except ValueError as e:
                print("Invalid choice. Please enter a valid choice 1 or 2.")


    except ValueError as e:
        print("Invalid choice. Please enter a valid choice 1 or 2.")
        