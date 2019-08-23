class ParserArgument:
    def __init__(self, url: str, mock: str = None):
        self.url = url
        self.mock = mock

    def has_mock(self):
        return self.mock is not None
