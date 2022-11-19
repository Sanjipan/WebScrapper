from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re


class WebScrapper:
    @staticmethod
    def Requests_of_html():
        user_url = str(input('[*] Enter Target URL to Scan:'))
        urls = deque([user_url])
        screapped_url = set()
        emails = set()
        count = 0
        try:
            while len(urls):
                count += 1
                if count == 100:
                    break
                url = urls.popleft()
                screapped_url.add(url)
                parts = urllib.parse.urlsplit(url)
                base_url = '''{0.scheme}'://'{0.netloc}''', format(parts)

                path = url[:url.rfind('/') + 1] if '/' in parts.path else url
                print('[%d] Processing %s' % (count, url))

                try:
                    response = requests.get(url)
                except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                    continue
                new_emails = set(re.findall(r'[a-z0-9\. \-+_]+@[a-z0-9\. \-+_]+\.[a-z]', response.text, re.I))
                emails.update(new_emails)

                soup = BeautifulSoup(response.text, features='lxml')

                for anchor in soup.find_all('a'):
                    link = anchor.attrs['href'] if 'herf' in anchor.attrs else ''
                if link.startswith('/'):
                    link = path + link
                    if not link in url and not link in screapped_url:
                        urls.append(link)
        except KeyboardInterrupt:
            print("[-] Closing!")

        for mail in emails:
            print(mail)
