import requests

def get_pokemon_details(name):
    api_url=f"https://pokeapi.co/api/v2/pokemon/{name}"
    try:
        response=requests.get(api_url)
    
        if response.status_code==200:
            data=response.json()
            types=[t["type"]["name"] for t in data["types"]]
            abilities=[a["ability"]["name"] for a in data["abilities"]]
            return {"name": name, "type": types, "abilities": abilities}
        else:
            print(f"Error number: {response.status_code}")
    except:
        print("Request Error")