import requests

class HtmlDownloader(object):


    def download(self, url):
        if url is None:
            return None

        response = requests.get(url)

        if response.reason != 'OK':
            return None
        response.encoding = 'utf-8'
        return response.text