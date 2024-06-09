# Comienzo importando asyincio y aiohttp para poder hacer peticiones asincronas, de otra manera, el sitio tardaria mucho en cargarse.
import asyncio
import aiohttp
from django.shortcuts import render

# Funcion para que, al recibir la url, se realize una llamada y la respuesta la convierta en json.
async def fetch_pokemon(session, url):
    try:
        async with session.get(url) as response:
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Error al hacer la llamada a la API: {e}")
        return None

# Funcion para obtener la informacion necesaria para el proyecto, se hace la peticion y con los resultados ya en formato json, se empieza a rellenar los datos requeridos.
async def get_pokemon_data(request, filter_func):
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=50'
    async with aiohttp.ClientSession() as session:
        response = await fetch_pokemon(session, url)
        data = response['results']
        tasks = [fetch_pokemon(session, pokemon['url']) for pokemon in data]
        pokemon_data = await asyncio.gather(*tasks)
        filtered_data = []
        for pokemon, pokemon_response in zip(data, pokemon_data):
            if filter_func(pokemon_response):
                pokemon['name'] = pokemon_response['name']
                pokemon['id'] = pokemon_response['id']
                pokemon['types'] = [{'name': t['type']['name']} for t in pokemon_response['types']]
                pokemon['height'] = (float(pokemon_response['height']) / 10)
                pokemon['weight'] = (float(pokemon_response['weight']) / 10)
                pokemon['image_url'] = pokemon_response['sprites']['other']['official-artwork']['front_default']
                filtered_data.append(pokemon)
        return filtered_data

# A partir de aca, son funciones que se van a renderizar en la url que se le indique. La funcion lambda recibe como argumento "pokemon_response" que es un objeto y realiza la operacion para filtrar segun lo especificado
async def lista_pokemon(request):
    return render(request, 'MyApp/pokemon.html', {'pokemon_list': await get_pokemon_data(request, lambda pokemon_response: True)})

async def filtro_peso(request):
    return render(request, 'MyApp/filtro1.html', {'pokemon_list': await get_pokemon_data(request, lambda pokemon_response: 30 < (float(pokemon_response['weight']) / 10) < 80)})

async def filtro_grass(request):
    return render(request, 'MyApp/filtro2.html', {'pokemon_list': await get_pokemon_data(request, lambda pokemon_response: pokemon_response['types'][0]["type"]['name'] == "grass")})


# Aca se realiza un mapeo de los tipos para crear una lista nueva y comprobar si el tipo "Flying" se encuentra entre ellos, si la respuesta da "true" se comprueba la segunda condicion que es si la altura es mayor a 10
# El mapeo basicamente es lo que en javascript seria pokemon_response.types.map(t => t.type.name)
async def filtro_flying(request):
    return render(request, 'MyApp/filtro3.html', {'pokemon_list': await get_pokemon_data(request, lambda pokemon_response: ("flying" in [t["type"]["name"] for t in pokemon_response['types']]) and pokemon_response['height'] > 10)})

# Por ultimo, en esta funcion lo que se hace es agarrar nombre por nombre y seleccionar todos los caracteres en orden inverso para luego almacenarlo en la variable
async def filtro_contrario(request):
    data = await get_pokemon_data(request, lambda pokemon_response: True)
    for pokemon in data:
        pokemon['name'] = pokemon['name'][::-1]
    return render(request, 'MyApp/filtro4.html', {'pokemon_list': data})

