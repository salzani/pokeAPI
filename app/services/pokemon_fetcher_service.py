from ..http.requests_client import RequestsClient
from ..serializers.pokemon_serializer import PokemonSerializer

class PokemonFetcherService:
    @staticmethod
    def fetch_pokemon(name):
        name = name.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        res = RequestsClient.get(url)

        if res.status_code != 200:
            return {
                'error': "Couldn't find pokemon"
            }
        
        pokemon = res.json()
        
        return PokemonSerializer.as_json(pokemon)
