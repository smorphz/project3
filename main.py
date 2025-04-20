def assign(total_seats, first_class_fee, ticket):
    seats = [None] * total_seats
    taken_seats = 0

    while taken_seats < total_seats:
        print(f"\nPlease select your ticket, extra ${first_class_fee} for First Class flyers!")
        ticket = input("Economy, First Class, or Emergency: ").lower()

        if ticket == "economy":
            print("Please proceed to the next available Economy seat.")
        elif ticket == "first class":
            money = float(input("Insert Cash: $"))
            print("You entered: $", money)

            if money >= first_class_fee:
                change = money - first_class_fee
                print("Payment accepted. Please make your way to First Class.")
                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
            else:
                print("Insufficient funds, please select Economy.")
                continue
        elif ticket == "emergency":
            confirm = input("Do you accept responsibility to assist in case of emergency? (yes/no): ").lower()
            if confirm != "yes":
                print("You must accept responsibility to sit in the emergency row.")
                continue
            else:
                print("Thank you for your willingness to assist.")
        else:
            print("Invalid ticket type. Please enter Economy, First Class, or Emergency.")
            continue

        seat_number = int(input("Select a seat number (1 to 20): "))
        if seat_number < 1 or seat_number > total_seats:
            print("Invalid seat number. Please choose between 1 and 20.")
            continue

        if seats[seat_number - 1] is not None:
            print("Seat already taken. Choose another seat.")
            continue


        seats[seat_number - 1] = ticket.title()
        taken_seats += 1
        print(f"Seat {seat_number} assigned as {ticket.title()}.")

        more = input("Do you want to buy another seat? (yes/no): ").lower()
        if more != "yes":
            break

    print("\nFinal Seat Map:")
    for i in range(total_seats):
        status = seats[i] if seats[i] else "Available"
        print(f"Seat {i + 1}: {status}")


assign(20, 1000, "")