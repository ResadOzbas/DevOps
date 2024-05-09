greeting = input('Greeting: ').lower()


def bank(greeting):
    if greeting[:5] == 'hello':
        return '$0'

    if greeting[0] == 'h':
        return '$20'

    return '$100'


print(bank(greeting))
