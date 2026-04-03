def create_account():
    while True:
        try:
            user_name = input("Enter your name(If you want to quit, enter 'q'): ")

            if user_name.lower() == 'admin':
                print("Welcome Admin!")
            if len(user_name) < 4:
                print("Your name need consist at least 4 words!")
                continue
            if user_name == 'q':
                break

            while True:
                user_age = int(input("Enter your age: "))

                if user_age <= 0:
                    print("ValueError[Not less than 0(zero)]")
                    continue
                if user_age >= 100:
                    print("No Lie(Sean Paul & Dua Lipa)")
                    continue
                else:
                    break

            user_data = {
                'name': user_name,
                'age': user_age
            }

            with open("profile.json", "w", encoding="utf-8") as file:
                json.dump(user_data, file, indent=4)

            print("\n---- Your profile created succesfully! ----\n")
            break

        except ValueError:
            print("Only numbers!")
        except KeyboardInterrupt:
            print("\nProcess has stopped!")
            break