from threading import Thread
from os import mkdir

from src.http.http_client import Request
from src.parser.reg_parser import RegParser


def main():
    # get url
    advt_url = input('ADVT URL ⤵️\n')

    # get img src
    response = Request.get(advt_url)
    find_img = RegParser.find_img(response.data)
    path = RegParser.get_pretty_path(advt_url)
    
    if not find_img:
        print('Not found img');

    # crate dis dir
    mkdir(path)

    # download img
    for index, item in enumerate(find_img):
        Thread(target=Request.load_data, args=(item, index, path)).start()


if __name__ == '__main__':
    main()