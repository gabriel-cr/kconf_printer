import sys
import requests
from html.parser import HTMLParser

magic_word = "CONFIG_"
cateee_url = "https://cateee.net/lkddb/web-lkddb/"

class MyHTMLParser(HTMLParser):
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

    if not sys.argv[1][0:len(magic_word)] == magic_word:
        print("Run with kconf_printer.py CONFIG_some_config")
        exit(1)

    rconf = sys.argv[1][len(magic_word):]

    try:
        r = requests.get("%s%s.html" %(cateee_url, rconf))
        parser = MyHTMLParser()
        parser.feed(r.content.decode('UTF-8'))
        exit(0)
        r = bf.find_all()
        
        for i in range(0, len(r)):
            if r[i].name == "h2" and r[i].get_text() in headers:
                print('\n------------')
                print(r[i].get_text())
                print('============')
                print(remove_ads(r[i + headers[r[i].get_text()]].get_text()))

    except Exception as ex:
        print(ex)
        raise


if __name__ == '__main__':
    main()
