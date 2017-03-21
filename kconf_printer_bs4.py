import sys
import requests
from bs4 import BeautifulSoup

magic_word = "CONFIG_"
cateee_url = "https://cateee.net/lkddb/web-lkddb/"

headers = {
    "General informations" : 1,
    "Help text" : 1,
    "Hardware" : 3
}

remove_shit = [
    "Sources",
]

def remove_ads(text):
    for i in remove_shit:
        idx = text.find(i)
        text = text[0:idx]
    
    return text

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
        bf = BeautifulSoup(r.content, "html.parser")
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
