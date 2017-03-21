import sys
import requests
from html.parser import HTMLParser

magic_word = "CONFIG_"
cateee_url = "https://cateee.net/lkddb/web-lkddb/"

class dumb_parser(HTMLParser):
    do_print = False

    def handle_data(self, data):
        if data == "General informations":
            self.do_print = True
        if data == "Sources":
            self.do_print = False

        if self.do_print:
            sys.stdout.write(data)
            sys.stdout.flush()

def main():
    if not len(sys.argv) == 2:
        print("Run with kconf_printer.py CONFIG_some_config")
        exit(1)

    if sys.argv[1][0:len(magic_word)] == magic_word:
        rconf = sys.argv[1][len(magic_word):]
    else:
        rconf = sys.argv[1]

    try:
        r = requests.get("%s%s.html" %(cateee_url, rconf))
        parser = dumb_parser()
        parser.feed(r.content.decode('UTF-8'))

    except Exception as ex:
        print(ex)
        raise


if __name__ == '__main__':
    main()
