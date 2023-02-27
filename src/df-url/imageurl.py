import requests

def export(self, endpoint, id, key, html: str, css: str) -> str:
    data = { 'html': html, 'css': css }
    image = requests.post(url = endpoint, data = data, auth=(id, key))
    return image.json()['url']

