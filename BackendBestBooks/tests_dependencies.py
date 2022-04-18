class PathsBuilder:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/'
        self.__STANDARD_BOOKS_APP_PATH = 'books/'
        self.__CATEGORIES_URL = 'categories-lister/'

    def build_categories_url(self):
        return self.__STANDARD_BACKEND_URL + self.__STANDARD_BOOKS_APP_PATH + self.__CATEGORIES_URL
