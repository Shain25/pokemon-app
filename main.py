import random
from pokeapi import get_pokemon_details
from json_manager import load_pokemon, save_data

def get_random_pokemon():
    import requests
    url="https://pokeapi.co/api/v2/pokemon?limit=1200"
    response=requests.get(url)
    if response.status_code==200:
        pokemon_list=response.json()["results"]
        return random.choice(pokemon_list)["name"]
    return None
    

pokemon_data=load_pokemon()

while True:
    choice=input("Do you want to draw a Pokemon? yes/no ")
    if choice == "no":
        print("Goodbye!")
        break
    elif choice == "yes":
        chosen_pokemon=get_random_pokemon()
        if not chosen_pokemon:
            print("Error, Couldn't pick a Pokemon")
            continue
        
        if "pokemon" not in pokemon_data:
            pokemon_data["pokemon"]=[]
        existing_pokemon = next((p for p in pokemon_data["pokemon"] if p["name"] == chosen_pokemon), None)

        if existing_pokemon:
            print(f"The Pokemon {chosen_pokemon} already exists")
            print(f"Type: {existing_pokemon['type']}")
            print(f"Abilities: {existing_pokemon['abilities']}")
        else:
            print(f"Downloading new info about {chosen_pokemon}")
            new_pokemon = get_pokemon_details(chosen_pokemon)
            print(new_pokemon)
            if new_pokemon:
                save_data(new_pokemon)
                print(f"New Pokemon added")
                print(f"Type: {new_pokemon['type']}")
                print(f"Abilities: {new_pokemon['abilities']}")
            else:
                print("Error, couldn't download data")
    else:
        print("Please type yes or no")
