# Classe pokemon et fonction de recherche

import requests

from models.pokemon import Pokemon


# fonction de recherche de pokémon par intervalle
# retourne une liste de pokémons si possible, sinon rien
# 1 - 152 => first gen
def find_pokemon_by_range(start, end):
    if start < 0:
        return None

    r = requests.get(f'https://pokeapi.co/api/v2/pokemon?offset={str(start)}&limit={str(end-start)}')
    if r.status_code !=200:
        return None
    res = []
    count = 1
    for pokemon_json in r.json()['results']:
        pokemon_json['id'] = start+count
        res.append(pokemon_json)
        count = count + 1
    return res

# fonction de recherche de pokémon par le nom
# retourne une instance de Pokemon si trouvé, sinon rien
def find_pokemon_by_name(name,start=0,end=151):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(name)}?offset={str(start)}&limit={str(end-start)}')

    if r.status_code !=200 :
        return None

    result = r.json()
    return Pokemon(result["id"], result["name"], get_image_content(result["sprites"]["front_default"]), result["types"][0]["type"]["name"], result["height"], result["weight"])

# fonction de recherche de pokémon par id
# retourne une instance de Pokemon si trouvé, sinon rien.
def find_pokemon_by_id(id,start=0,end=151):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{str(id)}?offset={str(start)}&limit={str(end-start)}')

    if r.status_code !=200 :
        return None

    result = r.json()
    return Pokemon(result["id"], result["name"], get_image_content(result["sprites"]["front_default"]), result["types"][0]["type"]["name"], result["height"], result["weight"])

def get_image_content(image_url):
    r = requests.get(image_url, allow_redirects=True)
    if r.status_code != 200:
        return None
    return r.content