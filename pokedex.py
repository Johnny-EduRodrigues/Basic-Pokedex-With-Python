pokedex = {}

def adicionarPokemon():

    nome = input("Nome do pokémon: ").capitalize()
    tipo = input("Tipo do pokémon: ").capitalize()
    while True:
        numero = int(input("Número na pokédex: "))
        if numero in pokedex:
            print("Um pokemon já ocupa esse lugar")
            print("Tente outro lugar")
            continue
        elif numero not in pokedex:
            break
    
    pokedex[numero] = {"Nome": nome,"Tipo": tipo}
    print(f"{nome} foi adicionado a pokédex no número {numero}")
    
def buscarPokemon():
    number = int(input("Que número da pokédex você deseja ver? "))
    if number in pokedex:
        print(pokedex[number])
    else:
        print("Você não possui um pokémon alocado nesse lugar.")

def listaPokemon():
    if not pokedex:
        print("Você não adicionou nenhum pokémon a sua pokédex!")
        return
    for numero, detalhes in sorted(pokedex.items()):
        print(f"Número: {numero} | Nome: {detalhes['Nome']} | Tipo: {detalhes['Tipo']}")
 
def menu():
    while True:
        print("\n=== Menu da Pokédex ===")
        print("1 - Adicionar Pokémon")
        print("2 - Buscar Pokémon")
        print("3 - Ver a listagem")
        print("4 - Sair")
        escolha = int(input())
        if escolha == 1:
            adicionarPokemon()
        elif escolha == 2:
            buscarPokemon()
        elif escolha == 3:
            listaPokemon()
        elif escolha == 4:
            break
menu()

print("Muito Obrigado!")
