import requests

class RequestsClient:
    @staticmethod
    def get(url):
        return requests.get(url)
