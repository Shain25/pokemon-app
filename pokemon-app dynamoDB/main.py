import random
from pokeapi import get_pokemon_details
from dynamodb_manager import load_pokemon, save_data, get_pokemon_by_name

def get_random_pokemon():
    import requests
    url="https://pokeapi.co/api/v2/pokemon?limit=1500"
    response=requests.get(url)
    if response.status_code==200:
        pokemon_list=response.json()["results"]
        return random.choice(pokemon_list)["name"]
    return None

while True:
    choice=input("Do you want to draw a Pokemon? yes/no ")
    if choice == "no":
        print("Goodbye!")
        break
    elif choice == "yes":
        pokemon_data=load_pokemon()
        chosen_pokemon=get_random_pokemon()
        if not chosen_pokemon:
            print("Error, Couldn't pick a Pokemon")
            continue
        
        existing_pokemon = get_pokemon_by_name(chosen_pokemon)

        if existing_pokemon:
            print(f"The Pokemon {chosen_pokemon} already exists")
            print(f"Type: {', '.join(existing_pokemon['type'])}")
            print(f"Abilities: {', '.join(existing_pokemon['abilities'])}")
            if 'created_at' in existing_pokemon:
                print(f"Added to collection: {existing_pokemon['created_at']}") 
        else:
            print(f"Downloading new info about {chosen_pokemon}")
            new_pokemon = get_pokemon_details(chosen_pokemon)
            print(new_pokemon)
            if new_pokemon:
                save_data(new_pokemon)
                print(f"New Pokemon added")
                print(f"Type: {', '.join(new_pokemon['type'])}")
                print(f"Abilities: {', '.join(new_pokemon['abilities'])}")
            else:
                print("Error, couldn't download data")
    else:
        print("Please type yes or no")