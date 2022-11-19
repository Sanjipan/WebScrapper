import urllib.request
import time

email_file = open("email.txt", 'a')


# Extracting Emails
def extract_emails_from_url_text(url_text, email_regex):
    extracted_email = email_regex.findall(url_text)
    all_emails = []
    for email in extracted_email:
        all_emails.append(email[0])
    length = len(all_emails)
    print("\t [*] Number of Emails: %s\n" % length)
    seen = set()
    for email in all_emails:
        if email not in seen:
            seen.add(email)
            email_file.write(email + '\n')


# HTML PAGE READER
def html_page_reader(url, i, email_regex):
    try:
        start_time = time.time()
        headers = {'User-Agent': 'Mozilla/5.0'}
        requests = urllib.request.Request(url, None, headers)
        responce = urllib.request.urlopen(requests)
        url_html_page_reader = responce.read()
        url_text = url_html_page_reader.decode()
        print("%s.%s\t Fetched in:%s" % (i, url, (time.time() - start_time)))
        extract_emails_from_url_text(url_text, email_regex)
    except:
        pass


class WebScrapperLib:
    # Emails Leech Function
    @staticmethod
    def emails_leech_function(url, i, email_regex):
        try:
            html_page_reader(url, i, email_regex)
        except urllib.error.HTTPerror as err:
            if err.code == 404:
                try:
                    url = 'http://webcache.googleusercontent.com/search?q=cache:' + url
                    html_page_reader(url, i, email_regex)
                except:
                    pass
            else:
                pass
