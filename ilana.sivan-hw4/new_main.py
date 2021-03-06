from store import Store

POSSIBLE_ACTIONS = [
    'search_by_name',
    'search_by_hashtag',
    'add_item',
    'remove_item',
    'checkout',
    'exit'
]

ITEMS_FILE = 'items.yml'


def read_input():
    line = input('What would you like to do?')
    args = line.split(' ')
    return args[0], ' '.join(args[1:])


def main():
    store = Store(ITEMS_FILE)
    action, params = None, None
    while action != 'exit':

        action, params = read_input()

        if action not in POSSIBLE_ACTIONS:
            print('No such action...')
            continue
        if action == 'checkout':
            print(f'The total of the purchase is {store.checkout()}.')
            print('Thank you for shopping with us!')
            return
        if action == 'exit':
            print('Goodbye!')
            return
        try:
            items = getattr(store, action)(params)
            for item in items:
                print(item, "\n")
        except Exception as e:
            print(e)
    


if __name__ == '__main__':
    main()
