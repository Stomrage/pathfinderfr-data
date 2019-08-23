from bs4 import BeautifulSoup


class ParserContent:
    def __init__(self, url: str, content: BeautifulSoup):
        self.url = url
        self.content = content
