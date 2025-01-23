pokedex = {}


def addPokemon():
    name = input("Enter the Pokémon's name: ").capitalize()
    pokemon_type = input("Enter the Pokémon's type: ").capitalize()
    while True:
        try:
            number = int(input("Enter the Pokédex number: "))
            if number in pokedex:
                print("A Pokémon already occupies this number.")
                print("Please try another number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    pokedex[number] = {"Name": name, "Type": pokemon_type}
    print(f"{name} has been added to the Pokédex at number {number}!")


def searchPokemon():
    try:
        number = int(input("Which Pokédex number do you want to view? "))
        if number in pokedex:
            print(f"Number: {number} | Name: {pokedex[number]['Name']} | Type: {pokedex[number]['Type']}")
        else:
            print("No Pokémon is assigned to this number.")
    except ValueError:
        print("Please enter a valid number.")


def listPokemon():
    if not pokedex:
        print("You haven't added any Pokémon to your Pokédex!")
        return
    print("\n=== Pokédex ===")
    for number, details in sorted(pokedex.items()):
        print(f"Number: {number} | Name: {details['Name']} | Type: {details['Type']}")


def menu():
    while True:
        print("\n=== Pokédex Menu ===")
        print("1 - Add Pokémon")
        print("2 - Search Pokémon")
        print("3 - View Pokémon list")
        print("4 - Exit")
        
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                addPokemon()
            elif choice == 2:
                searchPokemon()
            elif choice == 3:
                listPokemon()
            elif choice == 4:
                print("Thank you for using the Pokédex!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


menu()
