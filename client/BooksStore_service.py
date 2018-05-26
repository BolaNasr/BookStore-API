# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.


class BooksStoreService:
    def __init__(self, client):
        self.client = client

    def books_byBookId_delete(self, bookId, headers=None, query_params=None, content_type="application/json"):
        """
        Remove book from the Store.
        It is method for DELETE /books/{bookId}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/books/" + bookId
        return self.client.delete(uri, None, headers, query_params, content_type)

    def books_byBookId_get(self, bookId, headers=None, query_params=None, content_type="application/json"):
        """
        Retrieve book-related information.
        It is method for GET /books/{bookId}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/books/" + bookId
        return self.client.get(uri, None, headers, query_params, content_type)

    def books_byBookId_put(self, data, bookId, headers=None, query_params=None, content_type="application/json"):
        """
        Update book information.
        It is method for PUT /books/{bookId}
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/books/" + bookId
        return self.client.put(uri, data, headers, query_params, content_type)

    def books_get(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for GET /books
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/books"
        return self.client.get(uri, None, headers, query_params, content_type)

    def books_post(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for POST /books
        """
        if query_params is None:
            query_params = {}

        uri = self.client.base_url + "/books"
        return self.client.post(uri, data, headers, query_params, content_type)