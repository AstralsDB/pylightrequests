class ErrorHandler:
    def __init__(self, code, message, description):
        self.code = code
        self.message = message
        self.description = description
    
    def __str__(self):
        return f'Error: {self.description} ({self.code}) {self.message}'

class RequestError(ErrorHandler):
    def __init__(self):
        super().__init__(code="E00", message="Request Error", description="An error occured while communicating with the server.")

class ResponseError(ErrorHandler):
    def __init__(self, data):
        super().__init__(code="E01", message="Response Error", description=f"Invalid response data: {data}")
