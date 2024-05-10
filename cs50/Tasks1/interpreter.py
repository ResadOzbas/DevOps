x, symbol, y = input('Expression: ').split(' ')


def calc(x, y):
    match symbol:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y


answer = calc(float(x), float(y))

print("{:.1f}".format(answer))
