from urllib.request import Request
from urllib.request import urlopen


class WebScrapper:
    # Parser
    @staticmethod
    def parser(url, *args, **kwargs):
        try:
            # Create Request Object
            request = Request(url, **kwargs)

            # Print Debug info
            print('[HTTP "%s" to URL: %s] ' % (Request.__dict__['get_method'](Request), url))

            # Make HTTP request to the target URL
            response = urlopen(request).read().decode(encoding='utf-8', errors='ignore')

            # init regex to prase HTML
            regex = r'''(< *\w+( +\w+( *= *[\"|'][^\"|^']+[\"|'])?)* */? *>)([^<]*)'''
            try:
                regex = args[0]
            except:
                pass
        except Exception as e:
            print('[Error]:'+str(e))


