class PokemonSerializer:
    @staticmethod
    def as_json(pokemon):
        abilities = list(map(lambda abilities: abilities['ability']['name'], pokemon['abilities']))
        moves = list(map(lambda moves: moves['move']['name'], pokemon['moves']))
        types = list(map(lambda types: types['type']['name'], pokemon['types']))

        return {
            'name': pokemon['name'],
            'abilities': abilities,
            'moves': moves,
            'types': types
        }
