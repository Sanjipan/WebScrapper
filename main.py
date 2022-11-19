import sys
import re
import WebScrapperLib
import time

email_regex = re.compile(r'''
    #example :
    #something-.+_@somedomin.com
    (
    ([a-zA-Z0-9_.+]+
    @
    [a-zA-Z0-9_.+]+)
    )
    ''', re.VERBOSE)

if __name__ == '__main__':
    start = time.time()
    url_file = open("urls.txt", 'r')
    i = 0
    for url_link in url_file.readlines():
        url_link = url_link.strip('\'"')
        i = i + 1
        WebScrapperLib.WebScrapperLib.emails_leech_function(url_link, i, email_regex)
    print("Elapsed Time: %s" % (time.time() - start))

    url_file.close()
    WebScrapperLib.email_file.close()

