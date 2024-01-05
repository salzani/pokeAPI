from app.services.pokemon_fetcher_service import PokemonFetcherService

if __name__ == '__main__':
    print('Pokedex\n')

    while True:
        pokemon_name = str(input('Choose a Pokemon (e to exit): '))

        if pokemon_name == 'e':
            break

        pokemon = PokemonFetcherService.fetch_pokemon(pokemon_name)

        print('\nloading...\n')

        if 'error' in pokemon:
            print(f'Error: {pokemon["error"]}\n')
            continue

        for key, value in pokemon.items():
            print(f'{key}:\t{value}\n')
