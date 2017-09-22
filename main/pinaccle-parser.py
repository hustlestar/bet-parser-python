# encoding=cp1251
import lxml.html as LH
import requests
import codecs

from main.Bet import Bet


class Pinaccle:
    def get_leagues_urls(self):
        user_id = 12345
        base_url = "https://www.pinnacle.com/en/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        r = requests.get(base_url, headers)

        # with codecs.open('main.html', 'w', encoding='utf-8') as output_file:
        #    output_file.write(r.text)

        main_page = r.text
        # print main_page
        tree = LH.fromstring(main_page)
        sidebar = tree.xpath('//aside/div/ul/li[@class="level-1 no-live "]')  # боковая панель
        print len(sidebar)
        urls_list = []
        if sidebar:
            list_element = sidebar[0].xpath('//ul/li[@class="level-2"]')  # подсписок видов спорта
            for x in range(0, len(list_element)):
                a_list = list_element[x].xpath(
                    '//ul/li/a[contains(@href, "/en/odds/match/soccer/")]')  # все ссылки на футбол
                for href in a_list:
                    urls_list.append(base_url[0:-4] + href.attrib['href'])
        return urls_list

    def run(self):
        print self.get_leagues_urls()
        pass


if __name__ == '__main__':
    Pinaccle().run()
