import requests


urls = [f'https://www.cnblogs.com/#p{page}' for page in range(1, 11)]


def craw(url):
    get = requests.get(url)
    print(len(get.text))
