def get_game_pin():
    while True:
        try:
            pin = int(input("Enter game PIN (5-7 digits): "))
            if 10000 <= pin <= 9999999:
                return pin
            print("PIN must be 5-7 digits!")
        except ValueError:
            print("Please enter numbers only")
