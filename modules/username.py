

def get_base_username():
    while True:
        name = input("Enter base username (e.g. 'Hacker'): ").strip()
        if name:
            return name
        print("Username cannot be empty!")
