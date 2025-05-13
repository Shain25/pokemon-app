import json

json_file="pokemons.json"

def load_pokemon():
    try:
        with open(json_file, "r") as file:
            content=file.read().strip()
            if not content:
                return {"pokemon":[]}
            return json.loads(content)
    except FileNotFoundError:
        return {"pokemon": []}
    
def save_data(pokemon_details):
    data=load_pokemon()
    data["pokemon"].append(pokemon_details)
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)
    print(f"The pokemon {pokemon_details['name']} saved successfully!")