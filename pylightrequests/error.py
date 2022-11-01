class Error(Exception):
    def __init__(self, msg):
        self.msg = msg

class ResponseError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The response is bad.")

class DecodeError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The response cannot be decoded.")

class ProxyError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The request cannot use proxy.")

class TimeoutError(Error):
    def __init__(self, url):
        self.url = url
        super().__init__("The request is timeout.")

class BadRequestError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The request is bad.")

class SSLError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The request cannot use SSL.")

class RequestError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The request is failed.")

class GetError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The GET request is failed.")

class PostError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The POST request is failed.")

class PutError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The PUT request is failed.")

class DeleteError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The DELETE request is failed.")

class MethodError(Error):
    def __init__(self, response):
        self.response = response
        super().__init__("The request is not supported.")
