import requests

def pick(pokename):
    print('*ABILITYES*')
    for i in pokename['abilities']:
        print(i['ability']['name'] )

    print('\n')


def basic(pokebasic):
    print('*TYPE*')
    for i in pokebasic['types']:
        print(i['type']['name'])

    print("\n")


def main():
    while True:

        global pokemon
        pokemon = str(input('Escolha o pokemon: '))
        api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        res = requests.get(api)


        if res.status_code == 200:
            poke = res.json()
            pick(poke)
            basic(poke)
        else:
            print(f"ERRO! O POKEMON '{pokemon}' não foi encontrado na base de dados.")


if __name__ == '__main__':
    main()
