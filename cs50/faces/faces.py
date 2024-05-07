def convert(str):
    str = str.replace(':)', '🙂', 1)
    str = str.replace(":(", '🙁')
    print(str)


convert(input())
