def read_headers():
    return read_content('request-headers.txt')


def read_querystring():
    return read_content('request-querystring.txt')


def read_content(filename):
    result = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            splited = line.split(": ", 1)
            result[splited[0]] = splited[1]

    return result


if __name__ == '__main__':
    headers = read_headers()
    print(headers)
    querystring = read_querystring()
    print(querystring)
