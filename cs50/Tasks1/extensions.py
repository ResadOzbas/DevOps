filename, extension = input('file name: ').lower().strip().split('.')

match '.' + extension:
    case '.gif':
        print('image/gif')
    case '.jpg':
        print('image/jpeg')
    case '.jpeg':
        print('image/jpeg')
    case '.png':
        print('image/png')
    case '.pdf':
        print('application/pdf')
    case '.txt':
        print('image/txt')
    case '.zip':
        print('image/zip')
    case _:
        print('application/octet-stream')
