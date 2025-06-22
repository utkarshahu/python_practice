import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_api(name):
    
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)
    
    if response.status_code==200:
        print("Data retrived!")
        data=response.json()
        return data

pokemon_name = "pikachu"
pokemon_info = get_pokemon_api(pokemon_name)

if pokemon_info:
    print(f"Pkemon Info {pokemon_info["name"]}")