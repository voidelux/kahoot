def get_bot_count():
    while True:
        try:
            count = int(input("Number of bots to join (1-60): "))
            if 1 <= count <= 60:
                return count
            print("Must be between 1-60")
        except ValueError:
            print("Please enter a number")
