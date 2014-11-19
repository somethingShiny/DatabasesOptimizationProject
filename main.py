#required imports
from read_input import get_query
from convert_query import convert

PROJECT = 'π'.encode('utf-8')
SELECT = '(sigma)'


def main():
    #Do stuff
    query = get_query()
    print(query)
    convert(query)
    exit()


if __name__ == '__main__':
    main()