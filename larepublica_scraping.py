import requests
import lxml.html as html

HOME_URL = 'https://www.larepublica.co/'
HOME_URL2 = 'https://visas.migracion.gob.pa/SIVA/verif_citas_beijing_es/'
XPATH_LINK_ARTICLE = '//h2/a/@href'
XPATH_LINK = '/html/body/table/tbody/tr/td/p/a'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            link_article = parsed.xpath(XPATH_LINK_ARTICLE)
            print(link_article)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()