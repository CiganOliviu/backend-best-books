class PathsBuilder:
    def __init__(self):
        self.__STANDARD_BACKEND_URL = 'http://localhost:8000/'
        self.__STANDARD_BOOKS_APP_PATH = 'books/'
        self.__STANDARD_APPCONFIG_APP_PATH = 'config/'
        self.__CATEGORIES_URL = 'categories-lister/'
        self.__NATIONALITIES_URL = 'nationalities-lister/'
        self.__AUTHORS_URL = 'authors-lister/'
        self.__BOOKS_URL = 'books-lister/'
        self.__SCHEMAS_URL = 'schemas-lister/'

    def build_categories_url(self):
        return self.__STANDARD_BACKEND_URL + self.__STANDARD_BOOKS_APP_PATH + self.__CATEGORIES_URL

    def build_nationalities_url(self):
        return self.__STANDARD_BACKEND_URL + self.__STANDARD_BOOKS_APP_PATH + self.__NATIONALITIES_URL

    def build_authors_url(self):
        return self.__STANDARD_BACKEND_URL + self.__STANDARD_BOOKS_APP_PATH + self.__AUTHORS_URL

    def build_books_url(self):
        return self.__STANDARD_BACKEND_URL + self.__STANDARD_BOOKS_APP_PATH + self.__BOOKS_URL

    def build_schemas_url(self):
        return self.__STANDARD_BACKEND_URL + self.__STANDARD_APPCONFIG_APP_PATH + self.__SCHEMAS_URL
